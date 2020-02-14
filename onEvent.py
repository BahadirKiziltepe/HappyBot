import os
import discord

reload = False
reWrite = False
checkLines = []
words = []
wordMap = {}
        
class EventProperties:
    def __init__(self, client):
        self.client = client
        
    def setDictionary(self):
        global reWrite
        
        file = open('toRespond.txt', 'r')
        dictionary = file.readlines()
        file.close()

        for lines in dictionary:
            words = lines.split('|')
            
            if '|' not in lines or len(words) != 2 or lines.count('|') >= 2:
                reWrite = True
                checkLines.append(lines)

        if reWrite:
            reWrite = False
            file = open('toRespond.txt', 'w')
    
            for lines in dictionary:
                if lines not in checkLines:
                    file.write(lines)
            
            file.close()
            
            file = open('toRespond.txt', 'r')
            dictionary = file.readlines()
            file.close()

        for lines in dictionary:
            words = lines.split('|')
            wordMap["$" + words[0]] = words[1]
        
    def Setup(self):
        @self.client.event
        async def on_message(message):
            channel = message.channel
            global reload
            global dictionary
            
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
              
            if message.content == "$Help":
                word = "Commands to respond: "
                for lines in dictionary:
                    words = lines.split('|')
                    word += "`" + words[0] + "` "
                    
                word += "\nCommands: `$Help`, `$ExtendDictionary|<insert word>|<insert word>`"
                await channel.send(word)
              
            elif message.content.startswith("$ExtendDictionary|"):
                reload = True
                
                words = message.content.split('|')
                file = open('toRespond.txt', 'a')
                file.write("\n" + words[1] + "|" + words[2])
                file.close()
                
            elif message.content.startswith("$DeleteWord|"):
                reload = True
                
                words = message.content.split('|')
                
                file = open('toRespond.txt', 'r')
                lines = file.readlines()
                file.close()
                
                file = open('toRespond.txt', 'w')
                for line in lines:
                    if line.strip('\n') != words[1] + "|" + words[2]:
                        file.write(line)
                        
                file.close()
                    
            elif message.content in wordMap:
                await channel.send(wordMap[message.content])