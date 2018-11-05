import requests

class RestTemplate:
    def get(self, url):
        return requests.get(url)
        
    def get_query_parameters(self, url, query):
        return requests.get(url, params=query)

    def post(self, url, body):
        return requests.post(url, data=body)