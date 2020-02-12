import os
import discord

class CallingNames:
    def __init__(self, client, guild):
        self.client = client
        self.guild = guild

    def callClientEvent(self):
        @self.client.event
        async def on_ready():
            for g in self.client.guilds:
                if g.name == self.guild:
                    break
        
            print(f'{self.client.user} has connected to Discord!')
            print(f'{g.name}(id : {g.id})')
    
            members = '\n - '.join([member.name for member in g.members])
            print(f'Guild Members:\n - {members}')