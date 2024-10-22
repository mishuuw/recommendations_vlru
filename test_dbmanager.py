import unittest
import sqlite3
from dbmanager import usersDB

class TestUsersDB(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовой базы данных
        self.db_path = 'test_users.db'
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS userinfo(
                                userid text,
                                username text,
                                email text,
                                password text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS favorites(
                                userid text,
                                eventid text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS purchases(
                                userid text,
                                eventid text)""")
        self.conn.commit()

    def tearDown(self):
        # Очистка после тестов
        self.cursor.execute("DROP TABLE userinfo")
        self.cursor.execute("DROP TABLE favorites")
        self.cursor.execute("DROP TABLE purchases")
        self.conn.commit()
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
        auth_result = usersDB.authorize('testuser', 'password')
        self.assertTrue(auth_result)
        auth_result = usersDB.authorize('testuser', 'wrongpassword')
        self.assertFalse(auth_result)

    def test_add_to_favorites(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        userid = user['userid']
        success = usersDB.add_to_favorites(userid, 'event1')
        self.assertTrue(success)

    def test_get_favorites(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        userid = user['userid']
        usersDB.add_to_favorites(userid, 'event1')
        favorites = usersDB.get_favorites(userid)
        self.assertIn('event1', favorites)

    def test_add_to_purchases(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        userid = user['userid']
        success = usersDB.add_to_purchases(userid, 'event1')
        self.assertTrue(success)

    def test_get_purchases(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        userid = user['userid']
        usersDB.add_to_purchases(userid, 'event1')
        purchases = usersDB.get_purchases(userid)
        self.assertIn('event1', purchases)

    def test_get_popular_events(self):
        user1 = usersDB.register_user('testuser1', 'test1@example.com', 'password')
        user2 = usersDB.register_user('testuser2', 'test2@example.com', 'password')
        usersDB.add_to_favorites(user1['userid'], 'event1')
        usersDB.add_to_favorites(user2['userid'], 'event1')
        popular_events = usersDB.get_popular_events()
        self.assertIn('event1', popular_events)

    def test_get_recommended_events(self):
        user = usersDB.register_user('testuser', 'test@example.com', 'password')
        userid = user['userid']
        usersDB.add_to_favorites(userid, 'event1')
        recommended_events = usersDB.get_recommended_events(userid)
        self.assertNotIn('event1', recommended_events)

if __name__ == '__main__':
    unittest.main()