import unittest
from flask_testing import TestCase
from master import app

class TestMaster(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_register_user(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('userid', response.json)

    def test_authorize_user(self):
        # зарег пользователя
        self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })

        # авторизуемся
        response = self.client.post('/authorize', json={
            'login': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json)

    def test_add_favorite(self):
        user_data = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }).json

        # добавим событие в избранное
        response = self.client.post('/addFavorite', json={
            'userID': user_data['userid'],
            'eventID': 'event1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Event added to favorites')

    def test_buy_event(self):
        user_data = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }).json

        # купим событие
        response = self.client.post('/buy', json={
            'userID': user_data['userid'],
            'eventID': 'event1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Event purchased')

    def test_get_popular_events(self):
        response = self.client.get('/getPopularEvents')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_favorite_list(self):
        user_data = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }).json

        # добавим событие в избранное
        self.client.post('/addFavorite', json={
            'userID': user_data['userid'],
            'eventID': 'event1'
        })

        # список избранных событий
        response = self.client.get(f'/getFavoriteList?userID={user_data["userid"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('event1', response.json)

    def test_get_purchase_list(self):
        user_data = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }).json

        # купим событие
        self.client.post('/buy', json={
            'userID': user_data['userid'],
            'eventID': 'event1'
        })

        # список купленных событий
        response = self.client.get(f'/getPurchaseList?userID={user_data["userid"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('event1', response.json)

    def test_get_event_data(self):
        response = self.client.get('/getEventData?eventID=event1')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertEqual(response.json['event_id'], 'event1')

    def test_get_recommended_events(self):
        user_data = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }).json

        # получим рекомендации
        response = self.client.get(f'/getRecommendedEvents?userID={user_data["userid"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
