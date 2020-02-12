import os
import discord

class Responding:
    def __init__(self, client, channel):
        self.client = client
        self.channel = channel
        
    def Setup(self):
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
        
           # if message.content == "$Hello":