import json
import pickle

class User():
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


with open('user_data.pickle', 'wb') as f:
    pickle.dump(USER_LIST,f)
    f.close

