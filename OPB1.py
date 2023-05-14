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


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


message_counts = {}  # Dictionary to store message counts per user

@bot.event
async def on_message(message):
    global pirate_crews
    global message_counts

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

user_characters = {}  # Dictionary to store user characters
available_character = None  # Variable to store the available character

@bot.command(aliases=["c", "C"])
async def catch(ctx, *, guess: str):
    global user_characters
    global available_character

    if not available_character:
        await ctx.send("No character is currently available to be caught.")
        return

    # Check if the caught character matches the available character (case-insensitive)
    if guess.lower() != available_character.lower():
        await ctx.send(f"You can only catch the currently available character, use !hint if you're unsure.")
        return

    # Get the array of characters for the user, or create a new array if it doesn't exist
    user_character_array = user_characters.get(ctx.author.id, [])

    # Generate a unique ID for the new character
    character_id = len(user_character_array) + 1

    # Create a dictionary representing the character
    character = {
        'id': character_id,
        'name': available_character
    }

    # Add the character to the user's character array
    user_character_array.append(character)

    # Update the dictionary entry for the user
    user_characters[ctx.author.id] = user_character_array

    await ctx.send(f"Congratulations, {ctx.author.mention}! You have caught {available_character} and assigned ID: {character_id}")

    # Clear the available_character variable
    available_character = None
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
    user1_crew = user_characters.get(ctx.author.id, [])
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
    print("test3")
    if reaction.message.author == bot.user:
        trade_message = reaction.message
        trade_request = trade_requests.get(user.id)
        print(trade_request)
        print(trade_message.id)
        if trade_request is not None and trade_message.id == trade_request[2]:
            print("test5")
            if str(reaction.emoji) == '✅':
                user1_id, user1_character_id, message_id = trade_request

                # Retrieve the trade details
                user1_crew = user_characters.get(user1_id, [])
                user2_crew = user_characters.get(user.id, [])
                print("test2")
                if user1_crew and user2_crew:
                    user1_character = user1_crew[user1_character_id - 1]
                    print("test1")
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
async def addcharacter(ctx, character_id: int):
    trade_request = trade_requests.get(ctx.author.id)

    if trade_request is not None:
        user1_id, message_id = trade_request

        if message_id == ctx.message.id:
            trade_requests.pop(ctx.author.id)

            # Store the trade details
            user1_character_id = character_id
            user2_character_id = None

            await ctx.send(f"{ctx.author.mention}, please ask {ctx.message.mentions[0].mention} to provide the ID of the character they want to trade.")

            def check(message):
                return message.author.id == ctx.message.mentions[0].id

            try:
                user2_character_id = await bot.wait_for('message', timeout=60.0, check=check)
                user2_character_id = int(user2_character_id.content)
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.message.mentions[0].mention} did not provide the character ID in time. Trade cancelled.")
                return

            # Perform the trade
            await ctx.send(f"{ctx.author.mention} has traded character ID {user1_character_id} with {ctx.message.mentions[0].mention}'s character ID {user2_character_id}.")
        else:
            await ctx.send("Please initiate a trade first before adding a character.")
    else:
        await ctx.send("Please initiate a trade first before adding a character.")

def get_character_id(user_id, character_name):
    pirate_crew = pirate_crews.get(user_id)
    if pirate_crew is not None:
        for i, character in enumerate(pirate_crew):
            if character.lower() == character_name:
                return i + 1
    return None

# Load pirate crews from the file if it exists
try:
    with open("pirate_crews.json", "r") as file:
        pirate_crews_data = file.read()
        pirate_crews = eval(pirate_crews_data)
except FileNotFoundError:
    pirate_crews = {}


# Run the bot using your token
bot.run("MTEwNjAxMzA1NTQ5OTg5NDg5Ng.GInnmk.9l22-WJfV96-RJwttBKEbCMnvBVOkzFHhMtWNw")