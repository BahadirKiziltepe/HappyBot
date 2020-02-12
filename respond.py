import os
import discord

class Responding:
    def __init__(self, client):
        self.client = client
        
    def Setup(self):
        @self.client.event
        async def on_message(message):
            channel = message.channel
            if message.author == self.client.user:
                return
        
            if message.content == "$Hello":
                #
