import asyncio
import discord
from discord.ext import commands 
#pip install cookies-discord-components
from discord import Reaction, User
from discord.utils import get
import random
from typing import Optional, Union
from character_dictionary_total import characters_pictures,Character
import json
import os.path
import numpy as np
import requests 
import io


# Add more characters and image links here...
class User():
    def __init__(self,name,characters,message_count,selected_character):
        self.name = name
        self.characters = characters
        self.message_count = message_count
        self.selected_character = selected_character


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
    
    if os.path.isfile('user_data.json'):
        with open('user_data.json') as f:
            data = json.load(f)
            f.close()

        for user in data:
            character_list = {}
            for key in data[user]['characters']:
                c = data[user]['characters'][key]
                character_list[int(key)] = Character(c['name'],c['exp'],c['level'],c['picture'],c['special_name'],c['description'])
            new_user = User(int(data[user]['name']),character_list,data[user]['message_count'],data[user]['selected_character'])
            user_list[int(user)] = new_user

    for user in user_list:
        print(f"{user_list[user].selected_character}")
    print(f"Logged in as {bot.user.name}")

message_counts = {}  # Dictionary to store message counts per user

@bot.event
async def on_message(message):
    global user_list
    global message_counts
    global spawned_character
    ctx = await bot.get_context(message)
    # Check if the author is the bot itself or a DM
    if message.author == bot.user or isinstance(message.channel, discord.DMChannel):
        return

    # Check if the author has a pirate crew list
    if user_list.get(message.author.id) is None:
        user_list[message.author.id] = User(message.author.id,{},0,None)
        print("here")
    print(f"{ctx.author.id}")
    print(f"{message.author.id}")
    if user_list[message.author.id].selected_character is not None:
        selected_character = user_list[message.author.id].characters[user_list[message.author.id].selected_character]
        selected_character.AddXp(1)

        print(f"{selected_character.exp}")

        if selected_character.exp >= selected_character.GetExpReq():
            selected_character.exp = 0
            selected_character.level += 1
            save()
            await ctx.send(f"{selected_character.GetName()} leveled up")

    # Update the message count for the user
    user_list[message.author.id].message_count += 1

    # Randomly determine the spawn threshold between 20 and 35 messages
    spawn_threshold = random.randint(20, 35)

    if user_list[message.author.id].message_count >= spawn_threshold:
        # Reset the message count for the user
        user_list[message.author.id].message_count = 0
        await spawn(ctx)

    await bot.process_commands(message)  # Process other commands


pirate_crew_page_numbers = {}
class PirateCrewView(discord.ui.View):
    def __init__(self,ctx, *, timeout: float | None = 180):
        self.ctx = ctx
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Back",style=discord.ButtonStyle.red)
    async def back_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if(not await self.check_interacter(interaction)):
            return
        DATA = await pirate_crew_display(self.ctx,back_or_forward=-1)
        embed = DATA[0]
        view = DATA[1]
        await interaction.response.edit_message(embed=embed,view=view) 
        self.stop()
        

    @discord.ui.button(label="Next",style=discord.ButtonStyle.green)
    async def next_button(self,interaction:discord.Interaction, button:discord.ui.Button):
        if(not await self.check_interacter(interaction)):
            return
        DATA = await pirate_crew_display(self.ctx,back_or_forward=1)
        embed = DATA[0]
        view = DATA[1]
        self.stop()
        await interaction.response.edit_message(embed=embed,view=view)
        

    async def check_interacter(self,interaction:discord.Interaction):
        return interaction.user.id == self.ctx.author.id

async def pirate_crew_display(ctx,pg_number = None, back_or_forward = None):
    global user_list
    user_character_array = user_list.get(ctx.author.id).characters

    pirate_crew = user_character_array.copy()
    
    if(pg_number == None):
        pg_number = pirate_crew_page_numbers[ctx.author.id] + back_or_forward

    # Format the pirate crew with character name and ID
    emoji_list = []
    crew_list = ""
    upper_limit = (pg_number * 10)
    array_length  = len(user_character_array)

    #emoji_list = DATA[1]
    view = PirateCrewView(ctx)
    if array_length < 10:
        view.back_button.disabled = True
        view.next_button.disabled = True
    
    if(array_length < upper_limit):
        view.next_button.disabled=True
    
    if(pg_number == 1):
        view.back_button.disabled = True
    
    modifier = 9
    if(upper_limit > array_length):
        modifier = 9 - (upper_limit - array_length)
        upper_limit = array_length

    for i in range(upper_limit - modifier, upper_limit + 1):
        if(pirate_crew[i].special_name):
            name_parts = pirate_crew[i].special_name.split()
        else:
            name_parts = pirate_crew[i].name.split()
        name_parts = [part.capitalize() for part in name_parts]
        formatted_name = " ".join(name_parts)
        
        response = requests.get(pirate_crew[i].picture)
                                    # ThreePiecec 1089719818225188974
                                    # Two Piece 233680080897966090
        #emoji = await bot.get_guild(1089719818225188974).create_custom_emoji(name='emoji_name', image=response.content)
        #emoji_list.append(emoji)
    
    
        #crew_list += f"ID: {i} - {formatted_name} - <:{emoji.name}:{emoji.id}> \n"
        crew_list += f"ID: {i} - {formatted_name}\n"
    
    
    embed = discord.Embed(title="Your Pirate Crew page 1", description=crew_list, color=discord.Color.blue())
    embed.set_footer(text="One Piece Bot")

    pirate_crew_page_numbers[ctx.author.id] = pg_number 
    return [embed,view]

    
@bot.command(aliases=['pc', 'crew'])
async def piratecrew(ctx, *, args=""):
    global user_list
    user_character_array = user_list.get(ctx.author.id).characters

    # Check if the user has caught a character
    if not user_character_array:
        await ctx.send("Your pirate crew is empty.")
        return

    DATA = await pirate_crew_display(ctx,1)
    embed = DATA[0]
    view = DATA[1]

    await ctx.send(embed=embed,view = view)

    #for emoji in emoji_list:
        #await emoji.delete()

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
        available_character = Character(f"{spawned_character}",0,1,character_image_url,characters_pictures[spawned_character][2][character_image_url_id],characters_pictures[spawned_character][3][character_image_url_id])
    else:
         available_character = Character(f"{spawned_character}",0,1,character_image_url,None,characters_pictures[spawned_character][3][character_image_url_id])
    
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
        if(available_character.special_name):
            await ctx.send(f"You caught {available_character.special_name}!")
        else:
            await ctx.send(f"You caught {available_character.name}!")
        # Reset the available character to None
        available_character = None
        save()

    else:
        await ctx.send("That's not the right character. Try again.")

@bot.command(aliases=["save","Save"])
async def save_command(ctx):
    save()


def save():
    global user_list
    json_str = json.dumps(user_list,default=lambda o: o.__dict__,indent=4)
    with open('user_data.json', 'w') as f:
        f.seek(0)
        f.write(json_str)
        f.truncate()


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

    # Trade Reaction
    if reaction.message.author == bot.user:
        trade_message = reaction.message
        trade_request = trade_requests.get(user.id)
        
        if trade_request is not None and trade_message.id == trade_request[2]:
                
            if str(reaction.emoji) == '✅':
                user1_id, user1_character_id, message_id = trade_request
                print(bot.get_user(int(user1_id)))
                print(user1_id)
                # Retrieve the trade details
                user1_crew = user_list.get(user1_id).characters
                user2_crew = user_list.get(user.id).characters
                
                if user1_crew and user2_crew:
                    user1_character = user1_crew[user1_character_id]
                    
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
                        
                        # if the selected character is being traded away default active character to first character in crew
                        if user_list[user1_id].selected_character == user1_character_id:
                            user_list[user1_id].selected_character = 1

                        if user_list[user.id].selected_character == user2_character_id:
                            user_list[user.id].selected_character = 1
                        
                        user2_character = user2_crew[user2_character_id]
                        user1_crew[user1_character_id] = user2_character
                        user2_crew[user2_character_id] = user1_character
                        
                        name_1 = user1_character.name if not user1_character.special_name else user1_character.special_name
                        name_2 = user2_character.name if not user2_character.special_name else user2_character.special_name
                        
                        await trade_message.channel.send(f"{user.mention} has accepted the trade! {bot.get_user(user1_id).mention} has successfully traded their character '{name_1}' with {user.mention}'s character '{name_2}'. Trade successful!")
                    except asyncio.TimeoutError:
                        await trade_message.channel.send(f"{user.mention}, you took too long to respond. Trade canceled.")
                else:
                    await trade_message.channel.send(f"{user.mention}, you don't have any characters to trade. Trade canceled.")

                trade_requests.pop(user.id)
                save()
            elif str(reaction.emoji) == '❌':
                trade_requests.pop(user.id)
                await trade_message.channel.send(f"{user.mention} has declined the trade request.")

@bot.command()
async def get_guild_id(ctx):
    guild_id = ctx.guild.id
    await ctx.send(f"The Guild ID is: {guild_id}")

@bot.command(aliases=['select'])
async def select_active_character(ctx,id = None):
    if(id == None):
        await ctx.send("Please Enter Id of character you want to select")
        return
    else:
        try:
            id = int(id)
        except ValueError:
            await ctx.send('Please Enter Id of character you want to select')
    
    if id > len(user_list[ctx.author.id].characters):
        await ctx.send("Please enter id of character you want to select")
        return
    
    if user_list[ctx.author.id].characters[id]:
        user_list[ctx.author.id].selected_character = id
        save()
        await ctx.send(f"{user_list[ctx.author.id].characters[user_list[ctx.author.id].selected_character].GetName()}")
    else:
        await ctx.send("Please enter id of character you want to select")

    

bot.run("MTEwNzEzMjc3Mzc4Mjc5NDMzMA.GHq1OW.fbObqJIKe32iNwsuA7L_fStSKxUlBKXKZnZyiU")