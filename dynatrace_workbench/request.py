import requests


def get_dynatrace_headers(dynatrace_api_key, dynatrace_api_client):
    headers = dict()
    headers['accept'] = f'application/json'
    return headers

def post_request(url, headers, body):
    return True

def get_request(url, headers):
    return True

def delete_request(url, headers):
    return True

def put_request(url, headers, body):
    return True