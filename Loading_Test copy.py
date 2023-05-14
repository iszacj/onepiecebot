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


USER_LIST = {}

with open('user_data.pickle', 'rb') as f:
    USER_LIST = pickle.load(f)
    f.close()
    


