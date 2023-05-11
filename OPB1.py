import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

spawned_character = None  # Variable to store the currently spawned character
temporary_characters = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper"]  # Temporary list of characters

message_counter = 0
target_message_count = random.randint(5, 10)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!') or message.content.startswith('?'):  # Exclude bot commands
        return

    global spawned_character
    global message_counter
    global target_message_count

    message_counter += 1

    if message_counter >= target_message_count:
        if spawned_character is not None:
            await message.channel.send(f"The character {spawned_character} sailed away!")
            spawned_character = None

        message_counter = 0
        target_message_count = random.randint(5, 10)

    await bot.process_commands(message)

@bot.command()
async def spawn(ctx):
    global spawned_character

    if spawned_character is None:
        if not temporary_characters:
            await ctx.send("No characters available.")
            return
        
        spawned_character = random.choice(temporary_characters)
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

bot.run('')
