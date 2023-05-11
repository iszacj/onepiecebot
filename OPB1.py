import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


spawned_character = None  # Variable to store the currently spawned character
# temporary_characters = []  # Temporary list of characters

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Message tracking code
    for guild in bot.guilds:
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                # Track messages in text channels only
                # Increment the message counter
                pass

    await bot.process_commands(message)

@bot.command()
async def spawn(ctx):
    global spawned_character

    if spawned_character is None:
        characters = temporary_characters if temporary_characters else load_character_list()

        if not characters:
            await ctx.send("No characters available.")
            return
        
        spawned_character = random.choice(characters)
        # Code to send the image of the spawned character to the Discord channel
        await ctx.send(f"A One Piece character has been spawned! Guess the name using the command `!guess [name]`.")
        await ctx.send("Image of the character")  # Replace with code to send the character's image
    else:
        await ctx.send("A character has already been spawned. Guess the current character or wait for the next one.")

@bot.command()
async def hint(ctx):
    global spawned_character

    if spawned_character is not None:
        # Code to provide a hint by revealing 2-3 random letters of the character's name
        await ctx.send("Here's a hint: [Hint]")  # Replace [Hint] with the actual hint
    else:
        await ctx.send("No character has been spawned yet. Use the `!spawn` command to spawn a character.")

@bot.command()
async def guess(ctx, character_name):
    global spawned_character

    if spawned_character is not None:
        if character_name.lower() == spawned_character.lower():
            # Code to handle correct guess
            await ctx.send(f"Congratulations! You caught {spawned_character}.")  # Customize the success message
            spawned_character = None  # Reset spawned character
        else:
            # Code to handle incorrect guess
            await ctx.send("Incorrect guess. Try again or use the `!hint` command for a hint.")
    else:
        await ctx.send("No character has been spawned yet. Use the `!spawn` command to spawn a character.")

def load_character_list():
    with open('characters.txt', 'r') as file:
        return file.read().splitlines()

# Temporary list of characters
temporary_characters = [
    'Luffy',
    'Zoro',
    'Nami',
    'Usopp',
    'Sanji',
    'Chopper',
    'Robin',
    'Franky',
    'Brook',
    'Jinbe'
]

bot.run('MTEwNjAxMzA1NTQ5OTg5NDg5Ng.GUA5zD.iEkLngUcfwSDto1zJtcPQrVM-o9AAJ7ZeTMj3M')
