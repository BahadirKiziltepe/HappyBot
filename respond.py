import os
import discord

file = open('toRespond.txt', 'r')
dictionary = file.readlines()

words = []
wordMap = {}

for lines in dictionary:
    words = lines.split('||')
    wordMap["$" + words[0]] = words[1]

class Responding:
    def __init__(self, client):
        self.client = client
        
    def Setup(self):
        @self.client.event
        async def on_message(message):
            channel = message.channel
            if message.author == self.client.user:
                return
            
            if message.content in wordMap:
                await channel.send(wordMap[message.content])