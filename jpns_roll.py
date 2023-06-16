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



        


@client.event
async def on_ready():
    load_dotenv()
    
    print(f"ready to ROLL")


client.run(TOKEN)