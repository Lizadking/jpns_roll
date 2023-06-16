"""

"""


#Dependencies go here

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

#-------------------

#Main control here only, any and all other functions must be made in anothe file and imported 
intents = discord.Intents.default()
intents.message_content = True
description = ""
#bot's command prefix 
client = commands.Bot(command_prefix='/', description=description, intents=intents)
#get Identifier token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')


"""
function: on_read()
pre-condition: none
post-condition: initalized instance of the bot
comments: 
"""
@client.event
async def on_ready():

    #get the sync up ready for the slash commands 
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    #not much here, just thought it was cute to add 
    await client.change_presence(activity= discord.Game('with Servbots'),status=discord.Status.online)       
    
    print(f"ready to ROLL")


"""
function: help()
pre-condition: none
post-condition:displays help message
comments:  emphemeral -> the message only appears to the user 
"""
@client.tree.command(name="help")
async def help(interaction:discord.Interaction):
        #create the embed 
        not_done_yet_file = discord.File("wheres_that_feature.png",filename= "wheres_that_feature.png")
        message_embed =  discord.Embed()
        message_embed.set_image(url="attachment://wheres_that_feature.png")
        await interaction.response.send_message(file=not_done_yet_file,embed=message_embed,ephemeral= True)

client.run(TOKEN)