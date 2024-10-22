import unittest
import json
from flask import Flask
from master import app

class TestMaster(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register(self):
        response = self.app.post('/register', data=json.dumps({
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('userid', data)

    def test_authorize(self):
        self.app.post('/register', data=json.dumps({
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')

        response = self.app.post('/authorize', data=json.dumps({
            'login': 'testuser',
            'password': 'password'
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', data)

    def test_add_favorite(self):
        response = self.app.post('/addFavorite', data=json.dumps({
            'userID': 'testuserid',
            'eventID': 'event1'
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Event added to favorites')

    def test_buy(self):
        response = self.app.post('/buy', data=json.dumps({
            'userID': 'testuserid',
            'eventID': 'event1'
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Event purchased')

    def test_get_popular_events(self):
        response = self.app.get('/getPopularEvents')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_favorite_list(self):
        response = self.app.get('/getFavoriteList?userID=testuserid')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_purchase_list(self):
        response = self.app.get('/getPurchaseList?userID=testuserid')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_event_data(self):
        response = self.app.get('/getEventData?eventID=event1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_get_recommended_events(self):
        response = self.app.get('/getRecommendedEvents?userID=testuserid')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()