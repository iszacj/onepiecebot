import discord
from discord.ext import commands
import random
import json

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

characters = {
    "Luffy": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078788984520805/luffy.png",
    "Zoro": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078924347297812/zoro.png",
    "Nami": "https://cdn.discordapp.com/attachments/1106078732457873459/1106079299460669480/nami.png",
    "Usopp": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078924015935558/usopp.png",
    "Sanji": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078923613286440/sanji.png",
    "Chopper": "https://cdn.discordapp.com/attachments/1106078732457873459/1106078922795393035/chopper.png"
}

pirate_crews = {}  # Dictionary to store pirate crews


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command(aliases=["s"])
async def spawn(ctx):
    global pirate_crews

    if pirate_crews.get(ctx.author.id) is None:
        pirate_crews[ctx.author.id] = []  # Create an empty list for the user's pirate crew

    if len(pirate_crews[ctx.author.id]) == len(characters):
        await ctx.send("You have already caught all the characters.")
        return

    spawned_character = random.choice(list(set(characters.keys()) - set(pirate_crews[ctx.author.id])))
    character_image_url = characters[spawned_character]

    await ctx.send(f"A One Piece character has been spawned! Catch the character using the command `!catch [name]`.")
    await ctx.send(character_image_url)  # Send the character's image URL


@bot.command(aliases=["c"])
async def catch_character(ctx, character_name):
    global pirate_crews

    if pirate_crews.get(ctx.author.id) is None:
        pirate_crews[ctx.author.id] = []  # Create an empty list for the user's pirate crew

    if character_name.capitalize() not in characters:
        await ctx.send("Invalid character name.")
        return

    if character_name.capitalize() in pirate_crews[ctx.author.id]:
        await ctx.send("You have already caught this character.")
        return

    pirate_crews[ctx.author.id].append(character_name.capitalize())
    await ctx.send(f"{character_name.capitalize()} has joined your pirate crew!")


@bot.command(aliases=['pc', 'crew'])
async def piratecrew(ctx):
    pirate_crew = pirate_crews.get(ctx.author.id, [])

    if not pirate_crew:
        await ctx.send("Your pirate crew is empty.")
        return

    pirate_crew.sort()
    crew_list = "\n".join(pirate_crew)

    embed = discord.Embed(title="Your Pirate Crew", description=crew_list, color=discord.Color.blue())
    embed.set_footer(text="One Piece Bot")
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass  # Ignore command not found errors

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the name of the character.")

    else:
        await ctx.send(f"An error occurred: {type(error).__name__}")


@bot.event
async def on_disconnect():
    with open("pirate_crews.json", "w") as file:
        json.dump(pirate_crews, file)

@bot.command(aliases=['t'])
async def trade(ctx, other_user: discord.Member, your_character: str, their_character: str):
    # Convert character names to lowercase for case-insensitive search
    your_character = your_character.lower()
    their_character = their_character.lower()

    # Check if the characters are valid and owned by the respective users
    if not any(char.lower() == your_character for char in pirate_crews[ctx.author.id]):
        await ctx.send(f"You don't own the character {your_character}. Correct usage: `!trade (user) (your character) (their character)`")
        return

    if not any(char.lower() == their_character for char in pirate_crews[other_user.id]):
        await ctx.send(f"{other_user.mention} doesn't own the character {their_character}. Correct usage: `!trade (user) (your character) (their character)`")
        return

    # Perform the trade
    pirate_crews[ctx.author.id] = [char if char.lower() != your_character else their_character for char in pirate_crews[ctx.author.id]]
    pirate_crews[other_user.id] = [char if char.lower() != their_character else your_character for char in pirate_crews[other_user.id]]

    await ctx.send(f"{ctx.author.mention}, you have successfully traded your {your_character} with {other_user.mention}'s {their_character}.")


# Load pirate crews from the file if it exists
try:
    with open("pirate_crews.json", "r") as file:
        pirate_crews = json.load(file)
except FileNotFoundError:
    pirate_crews = {}

bot.run("")