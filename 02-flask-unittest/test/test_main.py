import unittest
from main import app
from unittest.mock import patch

class TestApi(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_main_page(self):
        resp = self.client.get('/')
        self.assertIn('Hello, gFu', resp.get_data(as_text=True))

    @patch('func.MathFunc.get_random_point')
    def test_multiply(self, mock_func):
        mock_func.return_value = (8,6)
        resp = self.client.get('/')
        self.assertIn('24', resp.get_data(as_text=True))
