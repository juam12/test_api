import unittest
import json
from test.resources.properties import BASE_URL
from main.api.rest_template import RestTemplate
from main.api.services.response_ejemplo import ResponseEjemplo

class TestEjemplo(unittest.TestCase):
    def setUp(self):
        self.client_rest = RestTemplate() 

    def test_api_ok(self):
        query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
        r = self.client_rest.get_query_parameters(BASE_URL, query)
        self.assertEqual(r.status_code, 200)

    def test_post_ok(self):
        body = {'search':'Nanotechnology'}
        r = self.client_rest.post('https://en.wikipedia.org/w/index.php', body)
        assert r.status_code == 200

    def test_response_ok(self):
        r = self.client_rest.get(BASE_URL)
        r_ejemplo = ResponseEjemplo(r.json()['url'], r.json()['origin'])
        print(r_ejemplo.origin)
        print(r_ejemplo.url)
        print("----------- response -------------")
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
