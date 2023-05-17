import discord
from discord.ext import commands
from discord import Reaction, User
import random
from typing import Union
from character_dictionary_total import characters_pictures,Character
import pickle
import os.path

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
available_character = None  # Variable to store the available character

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
        spawn(message)

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
    crew_list = ""
    for character_id in pirate_crew:
        name_parts = pirate_crew[character_id].name.split()
        name_parts = [part.capitalize() for part in name_parts]
        formatted_name = " ".join(name_parts)
        crew_list += f"ID: {character_id} - {formatted_name}\n"

    embed = discord.Embed(title="Your Pirate Crew", description=crew_list, color=discord.Color.blue())
    embed.set_footer(text="One Piece Bot")
    await ctx.send(embed=embed)


@bot.command(aliases=["s"])
async def spawn(ctx):
    global user_list
    global available_character
    
    users_crew = user_list.get(ctx.author.id).characters

    unique_caught_characters = []
    for character in users_crew:
        if(not (character.name in unique_caught_characters)):
            unique_caught_characters.append(character.name)

    # Check if the user has caught all the characters
    if len(unique_caught_characters) == len(characters_pictures):
        await ctx.send("You have already caught all the characters.")
        return

    # Randomly select a character that the user hasn't caught yet
    available_characters = list(set(characters_pictures.keys()) - set([character['name'] for character in unique_caught_characters]))
    if not available_characters:
        await ctx.send("You have already caught all the characters.")
        return

    spawned_character = random.choice(available_characters)
    print(spawned_character)
    character_image_url = random.choice(characters_pictures[spawned_character])

    # Set the available character to the newly spawned character
    available_character = Character(len(user_list.get(ctx.author.id).characters) + 1,f"{spawned_character}",1,character_image_url)

    

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

    if available_character is None:
        await ctx.send("No character has been spawned. Use the `!spawn` command to spawn a character.")
        return

    hint = generate_hint(available_character.name)
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

    if available_character is None:
        await ctx.send("No character has been spawned. Use the `!spawn` command to spawn a character.")
        return

    # Check if the guess is correct
    if guess.lower() == available_character.name.lower():
        # Add the character to the user's pirate crew
        user_list[ctx.author.id].characters[len(user_list.get(ctx.author.id).characters) + 1] = available_character

        await ctx.send(f"You caught {available_character.name}!")
        # Reset the available character to None
        available_character = None
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

bot.run("MTEwNjAxMzA1NTQ5OTg5NDg5Ng.GkomoF.qwQXIJeAomTyika4rWWkS9_ED6ehEXzJ5E43I8")