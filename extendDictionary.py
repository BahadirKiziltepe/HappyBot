import os
import discord

file = open('toRespond.txt', 'a')

class Extending:
    def __init__(self, client):
        self.client = client
        
    def Extend(self):
        @self.client.event
        async def on_message(message):
            channel = message.channel
            if message.author == self.client.user:
                return
            
            if message.content == "$Extend Dictionary":
                return