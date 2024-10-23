import unittest
import sqlite3
from dbmanager import usersDB, eventsDB

class TestUsersDB(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовой базы данных
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.executescript("""
            CREATE TABLE userinfo(userid text, username text, email text, password text);
            CREATE TABLE favorites(userid text, eventid text);
            CREATE TABLE purchases(userid text, eventid text);
        """)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_register_user(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        self.assertIsInstance(user, dict)
        self.assertIn('userid', user)
        self.assertIn('username', user)
        self.assertIn('email', user)
        self.assertIn('password', user)

    def test_authorize(self):
        usersDB.register_user('testuser', 'test@example.com', 'password')
        auth = usersDB.authorize('testuser', 'password')
        self.assertTrue(auth)

    def test_add_to_favorites(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        success = usersDB.add_to_favorites(user['userid'], 'event1')
        self.assertTrue(success)

    def test_get_favorites(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        usersDB.add_to_favorites(user['userid'], 'event1')
        favorites = usersDB.get_favorites(user['userid'])
        self.assertIn('event1', favorites)

    def test_add_to_purchases(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        success = usersDB.add_to_purchases(user['userid'], 'event1')
        self.assertTrue(success)

    def test_get_purchases(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        usersDB.add_to_purchases(user['userid'], 'event1')
        purchases = usersDB.get_purchases(user['userid'])
        self.assertIn('event1', purchases)

    def test_get_popular_events(self):
        popular_events = usersDB.get_popular_events()
        self.assertIsInstance(popular_events, list)

    def test_get_recommended_events(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        recommended_events = usersDB.get_recommended_events(user['userid'])
        self.assertIsInstance(recommended_events, list)

class TestEventsDB(unittest.TestCase):

    def test_get_random_events(self):
        events = eventsDB.get_random_events()
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 700)

    def test_get_event_data(self):
        event_data = eventsDB.get_event_data('event1')
        self.assertIsInstance(event_data, dict)
        self.assertIn('event_id', event_data)
        self.assertIn('categories', event_data)
        self.assertIn('name', event_data)
        self.assertIn('desc', event_data)
        self.assertIn('cost', event_data)
        self.assertIn('date', event_data)
        self.assertIn('location', event_data)
        self.assertIn('program', event_data)
        self.assertIn('author', event_data)
        self.assertIn('likes', event_data)
        self.assertIn('dislikes', event_data)
        self.assertIn('views', event_data)

if __name__ == '__main__':
    unittest.main()