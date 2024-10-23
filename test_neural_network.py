import unittest
import sqlite3
import pandas as pd
from neural_network import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовой базы данных
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.executescript("""
            CREATE TABLE CategoriesOfUsers(
                UserID text,
                Category1 integer,
                Category2 integer,
                Category3 integer
            );
            INSERT INTO CategoriesOfUsers VALUES ('user1', 5, 3, 0);
            INSERT INTO CategoriesOfUsers VALUES ('user2', 0, 4, 2);
        """)
        self.conn.commit()

        # Создание экземпляра NeuralNetwork
        self.nn = NeuralNetwork()

    def tearDown(self):
        self.conn.close()

    def test_init(self):
        # Проверка, что объект NeuralNetwork создан
        self.assertIsInstance(self.nn, NeuralNetwork)

    def test_get_predictions(self):
        # Проверка, что метод get_predictions возвращает список предсказаний
        predictions = self.nn._NeuralNetwork__get_predictions('user1')
        self.assertIsInstance(predictions, list)
        self.assertTrue(all(isinstance(pred, tuple) for pred in predictions))

    def test_allocate_events(self):
        # Проверка, что метод allocate_events возвращает словарь с распределением слотов
        predictions = self.nn._NeuralNetwork__get_predictions('user1')
        allocation = self.nn._NeuralNetwork__allocate_events(predictions)
        self.assertIsInstance(allocation, dict)
        self.assertTrue(all(isinstance(value, int) for value in allocation.values()))

    def test_get_recommended_events(self):
        # Проверка, что метод get_recommended_events возвращает список рекомендованных событий
        predictions = self.nn._NeuralNetwork__get_predictions('user1')
        allocation = self.nn._NeuralNetwork__allocate_events(predictions)
        recommended_events = self.nn._NeuralNetwork__get_recommended_events(allocation)
        self.assertIsInstance(recommended_events, list)
        self.assertTrue(all(isinstance(event, dict) for event in recommended_events))

    def test_get_recommendations(self):
        # Проверка, что метод get_recommendations возвращает список рекомендованных событий
        recommendations = self.nn.get_recommendations('user1')
        self.assertIsInstance(recommendations, list)
        self.assertTrue(all(isinstance(event, dict) for event in recommendations))

if __name__ == '__main__':
    unittest.main()