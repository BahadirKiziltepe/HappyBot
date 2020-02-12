import os
import discord
from dotenv import load_dotenv
from respond import Responding

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

client = discord.Client()
channel = discord.channel

respond = Responding(client, channel)
respond.Setup()

    
client.run(token)