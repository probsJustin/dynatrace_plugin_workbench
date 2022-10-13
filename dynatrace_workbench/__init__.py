import os
import requests
import dynatrace_workbench.v1
import dynatrace_workbench.v2

class init:
    v1 = ""
    v2 = ""
    DYNATRACE_API_KEY = f'DYNATRACE_API_KEY'
    DYNATRACE_CLIENT = f'DYNATRACE_CLIENT'
    DYNATRACE_URL = f'DYNATRACE_URL'

    DYNATRACE_API_KEY_DATA = f''
    DYNATRACE_CLIENT_DATA = f''
    DYNATRACE_URL_DATA = f''

    def notify_user(self, message):
        print(message)
        return message

    def test(self, test_string):
        test_string = f'test string for dynatrace workbench'
        self.notify_user(test_string)
        return test_string

    def get_dynatrace_url(self):
        try:
            self.DYNATRACE_URL_DATA = os.getenv(self.DYNATRACE_URL)
        except Exception as error:
            self.notify_user(f'Not able to get dynatrace url')

    def get_dynatrace_api_key(self):
        try:
            self.DYNATRACE_API_KEY_DATA = os.getenv(self.DYNATRACE_API_KEY)
        except Exception as error:
            self.notify_user(f'Not able to get dynatrace api key')


    def get_dynatrace_api_client(self):
        try:
            self.DYNATRACE_CLIENT_DATA = os.getenv(self.DYNATRACE_CLIENT)
        except Exception as error:
            self.notify_user(f'Not able to get dynatrace api client')

    def __init__(self):
        self.notify_user(f'Getting environment variables')
        self.get_dynatrace_url()
        self.get_dynatrace_api_key()
        self.get_dynatrace_api_client()
        self.v1 = dynatrace_workbench.v1.v1()
        self.v2 = dynatrace_workbench.v2.v2()


    def get_dynatrace_headers(self):
        headers = dict()
        headers['authorization'] = f'Api-Token {self.DYNATRACE_API_KEY_DATA}'
        headers['accept'] = f'application/json'
        return headers


    def post_request(self, url, body):
        return requests.post(url, body, headers=self.get_dynatrace_headers())


    def get_request(self, url):
        return requests.get(url, headers=self.get_dynatrace_headers())


    def delete_request(self, url):
        return requests.delete(url, headers=self.get_dynatrace_headers())


    def put_request(self, url, body):
        return requests.put(url, body, headers=self.get_dynatrace_headers())
