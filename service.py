import json
from flask import jsonify

class Service():
    def __init__(self) -> None:
        json_open = open('qitta_json.json', 'r')
        self.json_load = json.load(json_open)

    def get_users(self):
        return self.json_load

    def get_user(self, user_id):
        return ""
