import os
import dynatrace_workbench.constants

def notify_user(message):
    print(message)
    return message

def test():
    test_string = f'test string for dynatrace workbench'
    notify_user(test_string)
    return test_string

def get_dynatrace_url():
    try:
        constants.DYNATRACE_URL_DATA = os.getenv(constants.DYNATRACE_URL)
    except Exception as error:
        notify_user(f'Not able to get dynatrace url')

def get_dynatrace_api_key():
    try:
        constants.DYNATRACE_API_KEY_DATA = os.getenv(constants.DYNATRACE_API_KEY)
    except Exception as error:
        notify_user(f'Not able to get dynatrace api key')


def get_dynatrace_api_client():
    try:
        constants.DYNATRACE_CLIENT_DATA = os.getenv(constants.DYNATRACE_CLIENT)
    except Exception as error:
        notify_user(f'Not able to get dynatrace api client')

def init_environment():
    notify_user(f'Getting environment variables')
    get_dynatrace_url()
    get_dynatrace_api_key()
    get_dynatrace_api_client()
