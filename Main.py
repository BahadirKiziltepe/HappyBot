import os
import discord
from dotenv import load_dotenv
from onEvent import EventProperties

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

client = discord.Client()

event = EventProperties(client)
event.setDictionary()
event.Setup()
    
client.run(token)