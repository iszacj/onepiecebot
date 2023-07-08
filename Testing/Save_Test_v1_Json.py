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

ZORO = Character('zoro',0)
USER_LIST = {}
USER_LIST[0] = User('Shazeel',[ZORO],None)

json_str =json.dumps(USER_LIST,default=lambda o: o.__dict__,indent=4)

with open('user_data.json', 'w') as f:
    f.write(json_str)

