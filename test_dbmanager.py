import unittest
import sqlite3
from dbmanager import usersDB, eventsDB

class TestUsersDB(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовой базы данных
        self.db = sqlite3.connect(':memory:')
        self.cursor = self.db.cursor()
        self.cursor.executescript("""
            CREATE TABLE userinfo(
                userid text,
                username text,
                email text,
                password text
            );
            CREATE TABLE favorites(
                userid text,
                eventid text
            );
            CREATE TABLE purchases(
                userid text,
                eventid text
            );
        """)
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_register_user(self):
        user_data = usersDB.register_user('testuser', 'test@example.com', 'password')
        self.assertIsInstance(user_data, dict)
        self.assertIn('userid', user_data)
        self.assertEqual(user_data['username'], 'testuser')
        self.assertEqual(user_data['email'], 'test@example.com')
        self.assertEqual(user_data['password'], 'password')

    def test_authorize(self):
        usersDB.register_user('testuser', 'test@example.com', 'password')
        auth_result = usersDB.authorize('testuser', 'password')
        self.assertTrue(auth_result)
        auth_result = usersDB.authorize('testuser', 'wrongpassword')
        self.assertFalse(auth_result)

    def test_add_to_favorites(self):
        user_data = usersDB.register_user('testuser', 'test@example.com', 'password')
        user_id = user_data['userid']
        success = usersDB.add_to_favorites(user_id, 'event1')
        self.assertTrue(success)
        favorites = usersDB.get_favorites(user_id)
        self.assertIn('event1', favorites)

    def test_add_to_purchases(self):
        user_data = usersDB.register_user('testuser', 'test@example.com', 'password')
        user_id = user_data['userid']
        success = usersDB.add_to_purchases(user_id, 'event1')
        self.assertTrue(success)
        purchases = usersDB.get_purchases(user_id)
        self.assertIn('event1', purchases)

    def test_get_popular_events(self):
        usersDB.register_user('testuser', 'test@example.com', 'password')
        user_data = usersDB.register_user('testuser2', 'test2@example.com', 'password2')
        usersDB.add_to_favorites(user_data['userid'], 'event1')
        usersDB.add_to_purchases(user_data['userid'], 'event1')
        popular_events = usersDB.get_popular_events()
        self.assertIsInstance(popular_events, list)
        self.assertIn('event1', popular_events)

    def test_get_recommended_events(self):
        usersDB.register_user('testuser', 'test@example.com', 'password')
        user_data = usersDB.register_user('testuser2', 'test2@example.com', 'password2')
        usersDB.add_to_favorites(user_data['userid'], 'event1')
        usersDB.add_to_purchases(user_data['userid'], 'event1')
        recommended_events = usersDB.get_recommended_events(user_data['userid'])
        self.assertIsInstance(recommended_events, list)
        self.assertNotIn('event1', recommended_events)

class TestEventsDB(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовой базы данных
        self.db = sqlite3.connect(':memory:')
        self.cursor = self.db.cursor()
        self.cursor.executescript("""
            CREATE TABLE Event_to_Category(
                EventID text,
                Categories text
            );
        """)
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_get_random_events(self):
        self.cursor.execute("""
            INSERT INTO Event_to_Category (EventID, Categories) VALUES ('event1', 'cat1;cat2'), ('event2', 'cat3')
        """)
        self.db.commit()
        events = eventsDB.get_random_events()
        self.assertIsInstance(events, list)
        self.assertTrue(all(isinstance(event, dict) for event in events))

    def test_get_event_data(self):
        self.cursor.execute("""
            INSERT INTO Event_to_Category (EventID, Categories) VALUES ('event1', 'cat1;cat2')
        """)
        self.db.commit()
        event_data = eventsDB.get_event_data('event1')
        self.assertIsInstance(event_data, dict)
        self.assertEqual(event_data['event_id'], 'event1')
        self.assertEqual(event_data['categories'], ['cat1', 'cat2'])

if __name__ == '__main__':
    unittest.main()
