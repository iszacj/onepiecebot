import discord
from discord.ext import commands
import random
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

global USER_LIST
USER_LIST = {}
class User():
    def __init__(self,name,characters,message_count):
        self.name = name
        self.characters = characters
        self.message_count = message_count

    def ConvertToDict(self):
        new_characters = []
        for character in self.characters:
            new_characters.append(character.__dict__)
        old_characters = self.characters
        self.characters = new_characters
        return(self.__dict__)
    
    def ConvertToClass(self):
        new_characters = []
        for c in self.characters:
            new_characters.append(Character(c.name,c.level))
        self.characters = new_characters

        

class Character():
    def __init__(self,name,level):
        self.name = name
        self.level = level


spawned_character = None  # Variable to store the currently spawned character
temporary_characters = {
    "Luffy": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078788984520805/luffy.png",
    "Zoro": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078924347297812/zoro.png",
    "Nami": "https://cdn.discordapp.com/attachments/1106078732457873459/1106079299460669480/nami.png",
    "Usopp": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078924015935558/usopp.png",
    "Sanji": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078923613286440/sanji.png",
    "Chopper": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078922795393035/chopper.png"
}  # Temporary dictionary of characters and their corresponding image URLs

import random

def generate_hint(character_name):
    name_list = list(character_name)
    hint_length = random.randint(1, len(character_name) // 2)  # Random length for the hint
    hint_indices = random.sample(range(len(character_name)), hint_length)  # Random indices for the hint letters
    hint = [name_list[i] if i in hint_indices else '_' for i in range(len(character_name))]
    formatted_hint = ' '.join(hint)  # Separate each character with a space for better visibility
    return f'`{formatted_hint}`'

message_counter = 0
target_message_count = 0

def is_file_empty(file_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exists and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

@bot.event
async def on_ready():
    with open('user_data3.json') as f:
        data = json.load(f)
        f.close()
        print(data)
    for user in data:
        character_list = []
        for c in data[user]['characters']:
            character_list.append(Character(c['name'],c['level']))
        USER_LIST[int(user)] = User(data[user]['name'],character_list,data[user]['message_count'])
        USER_LIST[int(user)].ConvertToClass()
        print(USER_LIST[int(user)].characters[0].name)    
        print(USER_LIST[int(user)].characters)
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    global spawned_character
    global message_counter
    global target_message_count

    if target_message_count == 0:
        target_message_count = random.randint(10, 20)

    message_counter += 1

    if message_counter >= target_message_count:
        if spawned_character is not None:
            await message.channel.send(f"The character {spawned_character} sailed away!")
            spawned_character = None

        message_counter = 0
        target_message_count = random.randint(10, 20)

    await bot.process_commands(message)

@bot.command(aliases=['s'])
async def spawn(ctx):
    global spawned_character

    if spawned_character is None:
        if not temporary_characters:
            await ctx.send("No characters available.")
            return
        
        spawned_character = random.choice(list(temporary_characters.keys()))
        character_image_url = temporary_characters[spawned_character]
        
        await ctx.send(f"A One Piece character has been spawned! Catch the character using the command `!catch [name]`.")
        await ctx.send(character_image_url)  # Send the character's image URL
    else:
        await ctx.send("A character has already been spawned. Catch the current character or wait for the next one.")

@bot.command(aliases=['h'])
async def hint(ctx):
    global spawned_character

    if spawned_character is not None:
        hint = generate_hint(spawned_character)
        await ctx.send(f"Here's a hint: {hint}")
    else:
        await ctx.send("No character has been spawned yet.")


@bot.command(aliases=['c'])
async def catch(ctx, character_name):
    global spawned_character

    if spawned_character is not None:
        if character_name.lower() == spawned_character.lower():
            # Code to handle correct catch
            user = ctx.author
            if not(user.id in USER_LIST):
                USER_LIST[user.id] = User(user.id,[],0)
            USER_LIST[user.id].characters.append(Character(spawned_character,0))
            await ctx.send(f"Congratulations! You caught {spawned_character}. {spawned_character} has joined your pirate crew.")
            spawned_character = None  # Reset spawned character
        else:
            # Code to handle incorrect catch
            await ctx.send("Incorrect catch. Try again or use the `!hint` command for a hint.")
    else:
        await ctx.send("No character has been spawned yet. Use the `!spawn` command to spawn a character.")

@bot.command(aliases=['pc', 'crew'])
async def pirate_crew(ctx):
    user = ctx.author
    if user.id in USER_LIST:
        crew = USER_LIST[user.id].characters
        if crew:
            for character in crew:
                crew_list = f"{character.name} Lvl: {character.level}"
            response = f"```\nYour Pirate Crew:\n\n{crew_list}\n```"

            # Adjust the width of the response
            lines = response.split("\n")
            max_width = max(len(line) for line in lines)  # Find the maximum line width
            response = "```\n"
            response += "Your Pirate Crew:".ljust(max_width // 3 + 3) + "\n\n"  # Adjust the width of the title
            response += "\n".join(line.ljust(max_width // 3) for line in lines[3:])  # Adjust the width of the crew list
            response += "\n```"
            await ctx.send(response)
        else:
            print("here")
            await ctx.send("Your pirate crew is empty. Catch some characters using the `!catch` command!")
    else:
        print(ctx.author.id)
        await ctx.send("Your pirate crew is empty. Catch some characters using the `!catch` command!")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore command not found errors

    await ctx.send(f"An error occurred: {str(error)}")



@bot.event
async def on_member_join(member):
    if not(member.id in USER_LIST):
        USER_LIST[member.id] = User(member.id,[],0)

@bot.command(aliases=['sa'])
async def save(ctx):
    user_list = {}
    for user in USER_LIST:
        user_list[user] = USER_LIST[user].ConvertToDict()

    with open('user_data3.json', 'w') as f:
        json.dump(user_list,f,indent=4)
        f.close()
    print('Here')

@bot.command(aliases=['d'])
async def user_info(ctx):
    user_list = {}
    for user in USER_LIST:
        user_list[user] = USER_LIST[user].ConvertToDict()

    with open('user_data3.json', 'w') as f:
        print(json.dump(user_list,f,indent=4))
        f.close()
    

        
        
bot.run('MTEwNjAxMzA1NTQ5OTg5NDg5Ng.GHWs8M.6zyYYhVXJcYSuE_K7x3GYPWEqiU-D4BDQg8VxA')
