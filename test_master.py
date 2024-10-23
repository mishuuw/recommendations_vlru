import unittest
import json
from master import app
from dbmanager import usersDB, eventsDB
from flask_testing import TestCase
import sqlite3
from flask import Flask


class TestMaster(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.client = None

    @classmethod
    def setUpClass(cls):
        # Подготовка тестовой базы данных
        cls.test_db_path = 'test_users.db'
        cls.original_db_path = 'users.db'
        cls.backup_db_path = 'users_backup.db'

        # Создаем резервную копию оригинальной базы данных
        import shutil
        shutil.copyfile(cls.original_db_path, cls.backup_db_path)

        # Создаем тестовую базу данных
        shutil.copyfile(cls.original_db_path, cls.test_db_path)

        # Подключаемся к тестовой базе данных
        usersDB.db_path = cls.test_db_path
        eventsDB.db_path = 'dump.db'  # Убедитесь, что этот путь корректен

        # Создаем таблицы в тестовой базе данных
        usersDB.summon()

    @classmethod

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.app.post('/register', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('userid', response.json)

    def test_authorize(self):
        # Проверка авторизации зарегистрированного пользователя
        auth = usersDB.authorize('testuser', 'testpassword')
        self.assertTrue(auth)

    def test_add_favorite(self):
        # Сначала регистрируем пользователя
        self.test_register()

        data = {
            'userID': 'testuserid',
            'eventID': 'testeventid'
        }
        response = self.app.post('/addFavorite', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Event added to favorites')

    def test_buy(self):
        # Сначала регистрируем пользователя
        self.test_register()

        data = {
            'userID': 'testuserid',
            'eventID': 'testeventid'
        }
        response = self.app.post('/buy', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Event purchased')

    def test_get_popular_events(self):
        response = self.app.get('/getPopularEvents')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_favorite_list(self):
        # Сначала добавляем событие в избранное
        self.test_add_favorite()

        response = self.app.get('/getFavoriteList?userID=testuserid')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_purchase_list(self):
        # Сначала покупаем событие
        self.test_buy()

        response = self.app.get('/getPurchaseList?userID=testuserid')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)



if __name__ == '__main__':
    unittest.main()