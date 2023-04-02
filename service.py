import json

class Service():
    def __init__(self) -> None:
        json_open = open('users.json', 'r')
        self.json_load = json.load(json_open)

    def get_users(self):
        return self.json_load['users']

    def get_user(self, user_id):
        json_object = list(filter(lambda item : item['user_id'] == user_id, self.json_load['users']))
        return json_object[0]
