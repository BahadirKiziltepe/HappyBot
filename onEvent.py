import os
import discord
import re

dictionary = []
wordMap = {}
        
class EventProperties:    
    def __init__(self, client):
        self.client = client
        
    def setDictionary(self):
        global dictionary
        
        dictionary.clear()
        file = open('toRespond.txt', 'r')
        for line in file:
            words = line.strip('\n').split('|')
            if not line.strip('\n').isspace() and '|' in line.strip('\n') and line.strip('\n').count('|') == 1 and not words[0] == "" and not words[1] == "":
                dictionary.append(line)
        file.close()
        
        file = open('toRespond.txt','w')
        for line in dictionary:
            file.write(line)
            words = line.split('|')
            wordMap['$' + words[0]] = words[1]
        file.close()
        
    def editDictionary(Self, word):
        global dictionary
        
        dictionary.clear()
        file = open('toRespond.txt', 'r')
        for line in file:
            words = line.strip('\n').split('|')
            if not line.strip('\n').isspace() and '|' in line.strip('\n') and line.strip('\n').count('|') == 1 and not words[0] == "" and not words[1] == "" and not line.strip('\n') == word:
                dictionary.append(line)
        file.close()
        
        file = open('toRespond.txt','w')
        for line in dictionary:
            file.write(line)
            words = line.split('|')
            wordMap['$' + words[0]] = words[1]
        file.close()        
        
    def Setup(self):
        @self.client.event
        async def on_message(message):
            channel = message.channel
            global dictionary
            
            if message.author == self.client.user:
                return

            if message.content == "$Help" or message.content == "$":
                word = "Commands to respond: "
                for lines in dictionary:
                    words = lines.split('|')
                    word += "`" + words[0] + "` "
                    
                word += "\nCommands: `$(Help)`, `$(ExtendDictionary)(Extend)(E)|<i>|<i>`, `$(DeleteWord)(Delete)(D)|<i>|<i>`"
                await channel.send(word)
              
            elif message.content.startswith("$ExtendDictionary|") or message.content.startswith("$Extend|") or message.content.startswith("$E|"):                
                words = message.content.split('|')
                if len(words) == 3:
                    if not words[1] == "" and not words[2] == "":
                        file = open('toRespond.txt', 'a')
                        file.write("\n" + words[1] + "|" + words[2])
                        file.close()
                
                        self.setDictionary()
                        await channel.send("`" + (words[1] + "|" + words[2]) + "` Added to dictionary")
                    else:
                        await channel.send("Incorrect usage of command:\nKey words cannot be empty")
                else:
                    await channel.send("Incorrect usage of command:\nPlease enter your command in form of `$(ExtendDictionary)(Extend)(E)|<i>|<i>`")
                
            elif message.content.startswith("$DeleteWord|") or message.content.startswith("$Delete|") or message.content.startswith("$D|"):
                words = message.content.split('|')
                if len(words) == 3:
                    if not words[1] == "" and not words[2] == "":
                        if (words[1] + "|" + words[2]) in dictionary:
                            self.editDictionary((words[1] + "|" + words[2]))
                            await channel.send("`" + (words[1] + "|" + words[2]) + "` Deleted from dictionary")
                        else:
                            await channel.send("Dictionary does not contain `" + (words[1] + "|" + words[2]) + "`")
                    else:
                        await channel.send("Incorrect usage of command:\nKey words cannot be empty")
                else:
                    await channel.send("Incorrect usage of command:\nPlease enter your command in form of `$(DeleteWord)(Delete)(D)|<i>|<i>`")        
                
            elif message.content in wordMap:
                await channel.send(wordMap[message.content])