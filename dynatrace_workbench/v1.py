import json

class v1:
    spec = dict()

    def __init__(self):
        with open('./dynatrace_workbench/json/v1.json', 'r+') as json_file:
            self.spec = json.load(json_file)