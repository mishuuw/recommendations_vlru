import unittest
import sqlite3
import pandas as pd
from neural_network import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовой базы данных
        self.db = sqlite3.connect(':memory:')
        self.cursor = self.db.cursor()
        self.cursor.executescript("""
            CREATE TABLE CategoriesOfUsers(
                UserID text,
                cat1 int,
                cat2 int,
                cat3 int
            );
            INSERT INTO CategoriesOfUsers (UserID, cat1, cat2, cat3) VALUES ('user1', 5, 3, 1), ('user2', 2, 4, 5);
        """)
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_neural_network_initialization(self):
        nn = NeuralNetwork()
        self.assertIsInstance(nn, NeuralNetwork)
        self.assertIsNotNone(nn.algo)

    def test_get_predictions(self):
        nn = NeuralNetwork()
        predictions = nn._NeuralNetwork__get_predictions('user1')
        self.assertIsInstance(predictions, list)
        self.assertTrue(all(isinstance(pred, tuple) for pred in predictions))

    def test_allocate_events(self):
        nn = NeuralNetwork()
        predictions = nn._NeuralNetwork__get_predictions('user1')
        allocation = nn._NeuralNetwork__allocate_events(predictions)
        self.assertIsInstance(allocation, dict)
        self.assertEqual(sum(allocation.values()), 36)

    def test_get_recommended_events(self):
        nn = NeuralNetwork()
        predictions = nn._NeuralNetwork__get_predictions('user1')
        allocation = nn._NeuralNetwork__allocate_events(predictions)
        recommended_events = nn._NeuralNetwork__get_recommended_events(allocation)
        self.assertIsInstance(recommended_events, list)
        self.assertEqual(len(recommended_events), 36)

if __name__ == '__main__':
    unittest.main()
