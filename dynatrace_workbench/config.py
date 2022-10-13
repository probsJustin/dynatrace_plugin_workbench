import json

class config:
    spec = dict()

    def __init__(self):
        with open('./dynatrace_workbench/json/config.json', 'r+') as json_file:
            self.spec = json.load(json_file)