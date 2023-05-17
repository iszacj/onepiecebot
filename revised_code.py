import discord
from discord.ext import commands
from discord import Reaction, User
import random
from typing import Union
from character_dictionary_total import characters

# Add more characters and image links here...

# Setting up the bot with necessary intents
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix="!", intents=intents)

spawned_character = None  # Global variable to store the spawned character's name

pirate_crews = {}
user_characters = {}  # Dictionary to store user characters
available_character = None  # Variable to store the available character

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

message_counts = {}  # Dictionary to store message counts per user

@bot.event
async def on_message(message):
    global pirate_crews
    global message_counts
    global spawned_character

    # Check if the author is the bot itself or a DM
    if message.author == bot.user or isinstance(message.channel, discord.DMChannel):
        return

    # Check if the author has a pirate crew list
    if pirate_crews.get(message.author.id) is None:
        pirate_crews[message.author.id] = []

    # Update the message count for the user
    message_counts[message.author.id] = message_counts.get(message.author.id, 0) + 1

    # Randomly determine the spawn threshold between 20 and 35 messages
    spawn_threshold = random.randint(20, 35)

    if message_counts[message.author.id] >= spawn_threshold:
        # Reset the message count for the user
        message_counts[message.author.id] = 0

        # Randomly select a character that the user hasn't caught yet
        available_characters = list(set(characters.keys()) - set(pirate_crews.get(message.author.id, [])))
        if available_characters:
            spawned_character = random.choice(available_characters)
            character_image_url = characters[spawned_character]

            # Create an embedded message
            embed = discord.Embed(title="A One Piece character has been spawned!", color=discord.Color.blue())

            # Add the catch instructions and character image to the embed
            embed.add_field(name="Catch the character", value=f"Use the command `!catch [name]` to catch the character.", inline=False)
            embed.set_image(url=character_image_url)

            await message.channel.send(embed=embed)  # Send the embedded message

    await bot.process_commands(message)  # Process other commands

@bot.command(aliases=['pc', 'crew'])
async def piratecrew(ctx, *, args=""):
    global user_characters

    user_character_array = user_characters.get(ctx.author.id, [])

    # Check if the user has caught a character
    if not user_character_array:
        await ctx.send("Your pirate crew is empty.")
        return

    pirate_crew = user_character_array.copy()

    # Check the ordering option specified by the user
    if "-a" in args:
        pirate_crew.sort(key=lambda x: x['name'])  # Sort alphabetically by character name
    elif "-id" in args:
        pirate_crew.sort(key=lambda x: x['id'])  # Sort by character ID
    elif len(args) != 0:
        await ctx.send("Invalid ordering option. Use '-a' for alphabetical ordering or '-id' for ordering by ID.")
        return

    # Format the pirate crew with character name and ID
    crew_list = ""
    for character in pirate_crew:
        name_parts = character['name'].split()
        name_parts = [part.capitalize() for part in name_parts]
        formatted_name = " ".join(name_parts)
        crew_list += f"ID: {character['id']} - {formatted_name}\n"

    embed = discord.Embed(title="Your Pirate Crew", description=crew_list, color=discord.Color.blue())
    embed.set_footer(text="One Piece Bot")
    await ctx.send(embed=embed)


@bot.command(aliases=["s"])
async def spawn(ctx):
    global user_characters
    global available_character

    # Check if the user has caught all the characters
    if len(user_characters.get(ctx.author.id, [])) == len(characters):
        await ctx.send("You have already caught all the characters.")
        return

    # Randomly select a character that the user hasn't caught yet
    available_characters = list(set(characters.keys()) - set([character['name'] for character in user_characters.get(ctx.author.id, [])]))
    if not available_characters:
        await ctx.send("You have already caught all the characters.")
        return

    spawned_character = random.choice(available_characters)

    # Set the available character to the newly spawned character
    available_character = spawned_character

    character_image_url = characters[spawned_character]

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

    hint = generate_hint(available_character)
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
    global user_characters
    global available_character

    if available_character is None:
        await ctx.send("No character has been spawned. Use the `!spawn` command to spawn a character.")
        return

    # Check if the user has already caught the character
    if guess.lower() in [character['name'].lower() for character in user_characters.get(ctx.author.id, [])]:
        await ctx.send("You have already caught this character.")
        return

    # Check if the guess is correct
    if guess.lower() == available_character.lower():
        # Add the character to the user's pirate crew
        user_characters[ctx.author.id] = user_characters.get(ctx.author.id, []) + [{
            'name': available_character,
            'id': len(user_characters.get(ctx.author.id, [])) + 1
        }]

        # Reset the available character to None
        available_character = None

        await ctx.send(f"You caught {guess}!")

    else:
        await ctx.send("That's not the right character. Try again.")


bot.run("")