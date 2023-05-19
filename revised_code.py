import asyncio
import discord
from discord.ext import commands
from discord import Reaction, User
from discord.utils import get
import random
from typing import Union
from character_dictionary_total import characters_pictures,Character
import pickle
import os.path
import numpy as np
import requests 
import io
# Add more characters and image links here...
class User():
    def __init__(self,name,characters,message_count):
        self.name = name
        self.characters = characters
        self.message_count = message_count


# Setting up the bot with necessary intents
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix="!", intents=intents)

spawned_character = None  # Global variable to store the spawned character's name


user_list = {}  # Dictionary to store user characters
available_character = {}  # Variable to store the available character

@bot.event
async def on_ready():
    global user_list
    
    if os.path.isfile('user_data.pickle'):
        with open('user_data.pickle', 'rb') as f:
            user_list = pickle.load(f)
            f.close()
    print(f"Logged in as {bot.user.name}")

message_counts = {}  # Dictionary to store message counts per user

@bot.event
async def on_message(message):
    global user_list
    global message_counts
    global spawned_character

    # Check if the author is the bot itself or a DM
    if message.author == bot.user or isinstance(message.channel, discord.DMChannel):
        return

    # Check if the author has a pirate crew list
    if user_list.get(message.author.id) is None:
        user_list[message.author.id] = User(message.author.id,{},0)

    # Update the message count for the user
    user_list[message.author.id].message_count += 1

    # Randomly determine the spawn threshold between 20 and 35 messages
    spawn_threshold = random.randint(20, 35)

    if user_list[message.author.id].message_count >= spawn_threshold:
        # Reset the message count for the user
        user_list[message.author.id].message_count = 0
        await spawn(message)

    await bot.process_commands(message)  # Process other commands

@bot.command(aliases=['pc', 'crew'])
async def piratecrew(ctx, *, args=""):
    global user_list
    user_character_array = user_list.get(ctx.author.id).characters

    # Check if the user has caught a character
    if not user_character_array:
        await ctx.send("Your pirate crew is empty.")
        return

    pirate_crew = user_character_array.copy()


    # Check the ordering option specified by the user
    if "-a" in args:
        pirate_crew.sort(key=lambda x: x.name)  # Sort alphabetically by character name
    #elif "-id" in args:
       #// pirate_crew.sort(key=lambda x: x['id'])  # Sort by character ID
    elif len(args) != 0:
        await ctx.send("Invalid ordering option. Use '-a' for alphabetical ordering or '-id' for ordering by ID.")
        return

    # Format the pirate crew with character name and ID
    emoji_list = []
    crew_list = ""
    for character_id in pirate_crew:
        if(pirate_crew[character_id].special_name):
            name_parts = pirate_crew[character_id].special_name.split()
        else:
            name_parts = pirate_crew[character_id].name.split()
        name_parts = [part.capitalize() for part in name_parts]
        formatted_name = " ".join(name_parts)
        
        response = requests.get(pirate_crew[character_id].picture)
        emoji = await bot.get_guild(1089719818225188974).create_custom_emoji(name='emoji_name', image=response.content)
        emoji_list.append(emoji)
    
    
        
        crew_list += f"ID: {character_id} - {formatted_name} - <:{emoji.name}:{emoji.id}> \n"

    
    embed = discord.Embed(title="Your Pirate Crew", description=crew_list, color=discord.Color.blue())
    embed.set_footer(text="One Piece Bot")
    await ctx.send(embed=embed)

    for emoji in emoji_list:
        await emoji.delete()

@bot.command(aliases=["show"])
async def display_character(ctx,id):
    
    if(id == None):
        await ctx.send("Please Enter Id of character you want to see")
        return
    else:
        try:
            id = int(id)
        except ValueError:
            await ctx.send('Please Enter Id of character you want to see')
    
    print(user_list[ctx.author.id].characters)
    character_to_show = user_list[ctx.author.id].characters[id]
    print(character_to_show)

    if(character_to_show.special_name):
        name_parts = character_to_show.special_name.split()
    else:
        name_parts = character_to_show.name.split()
    name_parts = [part.capitalize() for part in name_parts]
    formatted_name = " ".join(name_parts)
    
    embed = discord.Embed(title=f"{formatted_name}", color=discord.Color.blue())
    embed.add_field(name="Level",value=f"{character_to_show.level}")
    embed.add_field(name="Description",value=character_to_show.description)
    embed.set_image(url=f"{character_to_show.picture}")
    await ctx.send(embed=embed)

@bot.command(aliases=["s"])
async def spawn(ctx):
    global user_list
    global available_character
    
    spawned_character = np.random.choice(list(characters_pictures.keys())
)
    print(spawned_character)
    Character_url_list = characters_pictures[spawned_character][0]
    temp_list = []
    for i in range(0,len(Character_url_list)):
        temp_list.append(i)

    character_image_url_id = np.random.choice(temp_list,p=characters_pictures[spawned_character][1])
    character_image_url = Character_url_list[character_image_url_id]
    special = False
    if(character_image_url_id != 0):
        special = True
        
    
    # Set the available character to the newly spawned character
    if(special):
        available_character[ctx.guild.id] = Character(f"{spawned_character}",1,character_image_url,characters_pictures[spawned_character][2][character_image_url_id],characters_pictures[spawned_character][3][character_image_url_id])
    else:
         available_character[ctx.guild.id] = Character(f"{spawned_character}",1,character_image_url,None,characters_pictures[spawned_character][3][character_image_url_id])
    
    if(special):
        embed = discord.Embed(title="A Special One Piece character has been spawned!", color=discord.Color.blue())
    else:
        # Create an embedded message
        embed = discord.Embed(title="A One Piece character has been spawned!", color=discord.Color.blue())

    # Add the catch instructions and character image to the embed
    embed.add_field(name="Catch the character", value=f"Use the command `!catch` to catch the character.", inline=False)
    embed.set_image(url=character_image_url)

    await ctx.send(embed=embed)  # Send the embedded message


@bot.command(aliases=['h'])
async def hint(ctx):
    global spawned_character
    global available_character

    if available_character[ctx.guild.id] is None:
        await ctx.send("No character has been spawned. Use the `!spawn` command to spawn a character.")
        return

    hint = generate_hint(available_character[ctx.guild.id].name)
    formatted_hint = " ".join(list(hint))

    embed = discord.Embed(title="Hint", description=f"Here's a hint for the spawned character:\n\n`{formatted_hint}`",
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


def generate_hint(character_name):
    hint = ""
    for c in character_name:
        if c.isalpha():
            hint += "_" if random.random() < 0.5 else c
        else:
            hint += c
    return hint


@bot.command(aliases=["c", "C"])
async def catch(ctx, *, guess: str):
    global user_list
    global available_character

    if available_character[ctx.guild.id] is None:
        await ctx.send("No character has been spawned. Use the `!spawn` command to spawn a character.")
        return

    # Check if the guess is correct
    if guess.lower() == available_character[ctx.guild.id].name.lower():
        # Add the character to the user's pirate crew
        user_list[ctx.author.id].characters[len(user_list.get(ctx.author.id).characters) + 1] = available_character[ctx.guild.id]
        if(available_character[ctx.guild.id].special_name):
            await ctx.send(f"You caught {available_character[ctx.guild.id].special_name}!")
        else:
            await ctx.send(f"You caught {available_character[ctx.guild.id].name}!")
        # Reset the available character to None
        available_character[ctx.guild.id] = None
        save()

    else:
        await ctx.send("That's not the right character. Try again.")

@bot.command(aliases=["save","Save"])
async def save_command(ctx):
    global user_list
    with open('user_data.pickle', 'wb') as f:
        pickle.dump(user_list,f)
        f.close

def save():
    global user_list
    with open('user_data.pickle', 'wb') as f:
        pickle.dump(user_list,f)
        f.close


global trade_requests
trade_requests = {}

@bot.command(aliases=['t'])
async def trade(ctx, other_user: discord.Member, user1_character_id: Union[int, str] = None):
    if user1_character_id is None:
        await ctx.send("Please provide the ID or name of the character you want to trade.")
        return

    if isinstance(user1_character_id, str):
        await ctx.send("Please provide the character ID instead of the character name.")
        return

    # Check if other_user is valid
    if other_user.bot or other_user == ctx.author:
        await ctx.send("Invalid trade request.")
        return

    # Check if user1_character_id is valid and owned by user1
    user1_crew = user_list.get(ctx.author.id).characters
    if not user1_crew:
        await ctx.send("You don't own any characters to trade.")
        return

    if user1_character_id < 1 or user1_character_id > len(user1_crew):
        await ctx.send(f"You don't own a character with ID {user1_character_id}.")
        return

    trade_message = await ctx.send(f"{other_user.mention}, {ctx.author.mention} wants to trade their character with ID {user1_character_id}. Do you accept? (React with ✅ or ❌)")
    
    await trade_message.add_reaction('✅')
    await trade_message.add_reaction('❌')

    trade_requests[other_user.id] = (ctx.author.id, user1_character_id, trade_message.id)

@bot.event
async def on_reaction_add(reaction: Reaction, user: User):
    if user == bot.user or user.bot:
        return
    
    if reaction.message.author == bot.user:
        trade_message = reaction.message
        trade_request = trade_requests.get(user.id)
        
        if trade_request is not None and trade_message.id == trade_request[2]:
            
            if str(reaction.emoji) == '✅':
                user1_id, user1_character_id, message_id = trade_request

                # Retrieve the trade details
                user1_crew = user_list.get(user1_id).characters
                user2_crew = user_list.get(user.id).characters
                
                if user1_crew and user2_crew:
                    user1_character = user1_crew[user1_character_id - 1]
                    
                    await trade_message.channel.send(f"{user.mention}, please enter the ID of the character you want to trade.")

                    def check_user2(m):
                        return m.author == user and m.channel == trade_message.channel

                    try:
                        user2_trade_response = await bot.wait_for('message', check=check_user2, timeout=60)
                        user2_character_id = int(user2_trade_response.content)

                        if user2_character_id < 1 or user2_character_id > len(user2_crew):
                            await trade_message.channel.send(f"{user.mention}, you don't own a character with ID {user2_character_id}. Trade canceled.")
                            trade_requests.pop(user.id)
                            return

                        user2_character = user2_crew[user2_character_id - 1]
                        user1_crew[user1_character_id - 1] = user2_character
                        user2_crew[user2_character_id - 1] = user1_character

                        await trade_message.channel.send(f"{user.mention} has accepted the trade! You have successfully traded your character '{user1_character['name']}' with {user.mention}'s character '{user2_character['name']}'. Trade successful!")
                    except asyncio.TimeoutError:
                        await trade_message.channel.send(f"{user.mention}, you took too long to respond. Trade canceled.")
                else:
                    await trade_message.channel.send(f"{user.mention}, you don't have any characters to trade. Trade canceled.")

                trade_requests.pop(user.id)
            elif str(reaction.emoji) == '❌':
                trade_requests.pop(user.id)
                await trade_message.channel.send(f"{user.mention} has declined the trade request.")

@bot.command()
async def get_guild_id(ctx):
    guild_id = ctx.guild.id
    await ctx.send(f"The Guild ID is: {guild_id}")

bot.run("MTEwNjAxMzA1NTQ5OTg5NDg5Ng.GBw3DZ.JIRtgh2Bu_KgoITRhBdusMPL_6sGzRjrZiPEcw")