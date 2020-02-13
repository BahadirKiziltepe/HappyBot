import os
import discord

reload = False
words = []
wordMap = {}

file = open('toRespond.txt', 'r')
dictionary = file.readlines()
file.close()

for lines in dictionary:
    words = lines.split('|')
    wordMap["$" + words[0]] = words[1]
        
class EventProperties:
    def __init__(self, client):
        self.client = client
        
    def Setup(self):
        @self.client.event
        async def on_message(message):
            channel = message.channel
            global reload
            
            if message.author == self.client.user:
                return
            
            if reload:
                reload = False
                
                file = open('toRespond.txt', 'r')
                dictionary = file.readlines()
                file.close()

                for lines in dictionary:
                    words = lines.split('|')
                    wordMap["$" + words[0]] = words[1]
                        
            if message.content.startswith("$ExtendDictionary|"):
                reload = True
                
                words = message.content.split('|')
                file = open('toRespond.txt', 'a')
                file.write("\n" + words[1] + "|" + words[2])
                file.close()
                
            elif message.content in wordMap:
                await channel.send(wordMap[message.content])