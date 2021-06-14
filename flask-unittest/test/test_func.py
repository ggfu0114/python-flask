import unittest

from codes.main import app


class TestFunc(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_main_func(self):
        resp = self.client.get('/')
        self.assertIn('gFu', resp.get_data(as_text=True))
