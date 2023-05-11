import json

class User(json.JSONEncoder):
    def __init__(self,name,characters,message_count):
        self.name = name
        self.characters = characters
        self.message_count = message_count

    def ConvertToDict(self):
        new_characters = []
        for character in self.characters:
            new_characters.append(character.__dict__)
        self.characters = new_characters
        return(self.__dict__)
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
    for character in data[user]['characters']:
        character_list.append(Character(character['name'],character['level']))
    USER_LIST[user] = User(data[user]['name'],character_list,data[user]['message_count'])
    print(USER_LIST[user].name)    
