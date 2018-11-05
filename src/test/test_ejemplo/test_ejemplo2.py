import unittest
import requests
from test.resources.properties import BASE_URL

class TestEjemplo2(unittest.TestCase):
    def setUp(self):
        pass

    def test_api_ok(self):
        r = requests.get(BASE_URL)
        print(r.text)
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
