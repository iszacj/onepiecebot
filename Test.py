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

ZORO = Character('zoro',0)
USER_LIST = {}
USER_LIST[0] = User('Shazeel',[ZORO],None)

user_list = {}
for user in USER_LIST:
    user_list[user] = USER_LIST[user].ConvertToDict()

with open('user_data.json', 'w') as f:
    json.dump(user_list,f,indent=4)
    f.close()
