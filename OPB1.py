import discord
from discord.ext import commands
import random
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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

@bot.event
async def on_ready():
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

user_scores = {}  # Dictionary to store user scores

user_crews = {}  # Dictionary to store user crews

user_crews = {}  # Dictionary to store user crews

@bot.command(aliases=['c'])
async def catch(ctx, character_name):
    global spawned_character

    if spawned_character is not None:
        if character_name.lower() == spawned_character.lower():
            # Code to handle correct catch
            user = ctx.author
            if user.id not in user_crews:
                user_crews[user.id] = set()
            user_crews[user.id].add(spawned_character)
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
    if user.id in user_crews:
        crew = sorted(user_crews[user.id])
        if crew:
            crew_list = "\n".join(crew)
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
            await ctx.send("Your pirate crew is empty. Catch some characters using the `!catch` command!")
    else:
        await ctx.send("Your pirate crew is empty. Catch some characters using the `!catch` command!")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore command not found errors

    await ctx.send(f"An error occurred: {str(error)}")



class User(json.JSONEncoder):
    def __init__(self,name,characters,message_count):
        self.name = name
        self.characters = characters
        self.message_count = message_count
    
    def default(self, o):
        return o.__dict__
    
class Character(json.JSONEncoder):
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def default(self, o):
        return o.__dict__

users_info = {}

@bot.event
async def on_member_join(member):
    if not(member.id in users_info):
        users_info[member.id] = User(member.id,None,None)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for member in guild.members:
           if not(member.id in users_info):
                users_info[member.id] = User(member.id,None,None)
                
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    
    
@bot.command()
async def show_user_data(ctx):
        await ctx.send(users_info)
        with open('user_data.json', 'w') as f:
            json.dump([user.__dict__ for user in users_info])

async def async_cleanup():  # example cleanup function
        with open('user_data.json', 'w') as f:

            json.dump([User.__dict__])

@bot.event
async def on_close(self):
    # do your cleanup here
    await self.async_cleanup()
    
    await self.close()  # don't forget this!

bot.run('MTEwNjAxMzA1NTQ5OTg5NDg5Ng.GrrSrf.ZH-Q84ySlS8AUm8lnJLKgktv6lbpyns7KehwME')
