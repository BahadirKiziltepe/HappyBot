import os
import discord
from dotenv import load_dotenv
from respond import Responding
from extendDictionary import Extending

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

client = discord.Client()

respond = Responding(client)
respond.Setup()

extend = Extending(client)
extend.Extend()

    
client.run(token)
