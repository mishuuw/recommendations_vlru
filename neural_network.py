import sqlite3, random
import pandas as pd
from math import floor
from dbmanager import eventsDB
from collections import defaultdict
from surprise import Dataset, Reader, accuracy, KNNBasic
from surprise.model_selection import train_test_split

class NeuralNetwork:
    def __init__(self):

        conn = sqlite3.connect('ratings.db')
        query = "SELECT * FROM CategoriesOfUsers"
        print(f'Converting .bd to Dataframe')
        df = pd.read_sql_query(query, conn)
        conn.close(); del query

        print('Melting Dataframe..')
        df_melted = df.melt(id_vars='UserID', var_name='Category', value_name='rating'); del df
        self.df_melted = df_melted[df_melted['rating'] > 0]; del df_melted
        self.all_categories = self.df_melted['Category'].unique()
        print('Making Dataset...')
        reader = Reader(rating_scale=(1, self.df_melted['rating'].max()))
        data = Dataset.load_from_df(self.df_melted[['UserID', 'Category', 'rating']], reader); del reader
        print('Splitting Dataset..')
        trainset, testset = train_test_split(data, test_size=0.2); del data
        self.algo = KNNBasic(sim_options={'name': 'cosine', 'user_based': False})
        print('Started training...')
        self.algo.fit(trainset); print('Done training, Testing..'); del trainset
        predictions = self.algo.test(testset); del testset
        accuracy.rmse(predictions);del predictions


    def __get_predictions(self, user_id,
                            num_recommendations = 9,
                            old_to_new_ratio = 0.7,):
        '''
        Using AI to predict event categories that user_id could like
        :param user_id: str: 32 - symbol ID
        :param num_recommendations: int: amount of predicted categories
        :param old_to_new_ratio: float: ratio of known categories to new categories
        :return:
        '''

        n_known = floor(num_recommendations*old_to_new_ratio)
        n_new = num_recommendations-n_known

        user_categories = self.df_melted[self.df_melted['UserID'] == user_id]['Category'].unique()
        categories_to_predict = [cat for cat in self.all_categories if cat not in user_categories]

        known_predictions = [self.algo.predict(user_id, category) for category in user_categories]
        known_predictions.sort(key=lambda x: x.est, reverse=True)

        new_predictions = [self.algo.predict(user_id, category) for category in categories_to_predict]
        new_predictions.sort(key=lambda x: x.est, reverse=True)

        top_new = [pred for pred in new_predictions[:n_new]]
        top_known = [pred for pred in known_predictions[:n_known]]

        recommendations = top_known + top_new
        recommendations.sort(key=lambda x: x.est, reverse=True)
        return recommendations

    @staticmethod
    def __allocate_events(recommendations,
                        total_slots=36,
                        min_events=2,
                        max_events=6):
        '''
        Allocating 36(default) slots between 9(default) predicted categories
        :param recommendations: list of Prediction() from NeuralNetwork.get_predictions()
        :param total_slots: int: amount of slots for events
        :param min_events: int: minimum amount of events per category
        :param max_events: int: maximum amount of events per category
        :return:
        '''
        total_weight = sum([prediction.est for prediction in recommendations])
        normalized_weights = {pred.iid: pred.est / total_weight for pred in recommendations}
        # bounding weight*total_slots to [2,6]
        allocation = {cat: max(min_events, min(int(weight * total_slots), max_events))
                      for cat, weight in normalized_weights.items()}

        allocated = sum(allocation.values())

        # Недобор - Выделяем самым большим по 1 по порядку
        if allocated < total_slots:
            remaining_slots = total_slots - allocated
            # Sorted by weight (more -> less)
            sorted_categories = sorted(normalized_weights.items(), key=lambda x: x[1], reverse=True)
            for cat, _ in sorted_categories:
                allocation[cat] += 1
                remaining_slots -= 1
                if remaining_slots == 0:
                    break

        # Перебор - Забираем у самых меньших по 1 по порядку
        elif allocated > total_slots:
            excess_slots = allocated - total_slots
            # Sorted by weight (less -> more)
            sorted_categories = sorted(normalized_weights.items(), key=lambda x: x[1])
            for cat, _ in sorted_categories:
                if allocation[cat] > min_events:
                    allocation[cat] -= 1
                    excess_slots -= 1
                if excess_slots == 0:
                    break

        return allocation

    @staticmethod
    def __get_recommended_events(allocation):
        '''
        Defining the recommended events based on category allocation
        :param allocation: dict: {category: amount]
        :return: list: [event_1, event_2, event_3, ...]
        '''

        # ПРЕДПОЛОГАЮ, что данные о событиях хранятся в файле 'events.db'
        # Тогда, вместо след. строки должна быть строка, берущая данные из БД.
        events = eventsDB.get_random_events()
        categorized_events = defaultdict(list)
        allocation_slots = sum(allocation.values())

        for event in events:
            for category in event['categories'][
                            ::-1]:  # Переворачиваю, т.к. (как мне показалось) главные категории справа.
                if category in allocation:
                    categorized_events[category].append(event)
        recommended_events = []; del events
        used_events = set()

        while len(recommended_events) < allocation_slots:
            keys = list(allocation.keys())
            for i, category in enumerate(keys):
                num_slots = allocation[category]

                events_for_category = categorized_events[category]
                events_for_category = [event for event in events_for_category if event['event_id'] not in used_events]

                # НА ЭТОМ ЭТАПЕ ВАЖНО ОТСОРТИРОВАТЬ СОБЫТИЯ ПО КАКОМУ ЛИБО ПАРАМЕТРУ (ВНУТРЕННЯЯ ЛОГИКА VL.RU),
                # Я ИСПОЛЬЗУЮ РАНДОМНЫЙ ПАРАМЕТР views, от больших к меньшим.
                events_for_category.sort(key=lambda x: x['views'], reverse=True)
                selected_events = events_for_category[:num_slots]
                remaining_slots = num_slots - len(selected_events)

                allocation[category] = remaining_slots
                if remaining_slots > 0:
                    allocation.pop(category)  # there is no more events of such category, removing

                recommended_events.extend(selected_events)
                used_events.update([event['event_id'] for event in selected_events])

            remaining_slots = allocation_slots - len(recommended_events)
            keys = list(allocation.keys())
            # dividing remaining slots between remaining categories
            while remaining_slots > 0:
                for category in keys:
                    allocation[category] += 1
                    remaining_slots -= 1
                    if remaining_slots == 0:
                        break
        recommended_events.sort(key=lambda x: x['views'], reverse=True)
        return recommended_events

    def get_recommendations(self, user_id):
        predictions = self.__get_predictions(user_id)
        allocation = self.__allocate_events(predictions)
        recommendations = self.__get_recommended_events(allocation); del predictions; del allocation
        return recommendations