import json

class User(json.JSONEncoder):
    def __init__(self,name,characters,message_count):
        self.name = name
        self.characters = characters
        self.message_count = message_count

class Character():
    def __init__(self,name,level):
        self.name = name
        self.level = level


USER_LIST = {}

with open('user_data.json') as f:
    data = json.load(f)
    f.close()

for user in data:
    character_list = []
    for c in data[user]['characters']:
        character_list.append(Character(c['name'],c['level']))
    new_user = User(data[user]['name'],character_list,data[user]['message_count'])
    USER_LIST[user] = new_user

