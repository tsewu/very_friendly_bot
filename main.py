"""
Author:      Roy Wu
Description: very 1st Discord bot
History:     05/25/2021 - intial version
Referebce:   https://www.youtube.com/watch?v=SPTfmiYiuok
"""

import discord
import json
import os       #* use token
import random
import requests #* get data from API
#from replit import db

client = discord.Client()

sadWords = ["sad", 
  "depressed", 
  "depressing", 
  "miserable", 
  "unhappy", 
  "not happy"]

encourage = [
  "Cheer up!",
  "Hang in there",
  "Maybe talk to Dr. Wu?",
  "What doesn’t kill you makes you stronger."]


#*---------- ----------
#*    get quote from an API
#*---------- ----------
def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] #* API syntax
  return(quote) 


@client.event
async def on_ready():
  print('Woohoo~ we have loggin as {0.user}'.format(client))


@client.event
async def on_message(msg):
  #msgContent = msg.content

  if msg.author == client.user:
    return

  if msg.content.startswith('$hello'):
    await msg.channel.send('Konnichi wa!')  

  if msg.content.startswith('$inspire me'):
    quote = getQuote()
    await msg.channel.send(quote)  

  #* if any words are in the sadWord, say random encourage message
  if any(word in msg.content for word in sadWords):
    await msg.channel.send(random.choice(encourage))    


#*---------- ----------
#*    OAuth2 bot token is placed here
#*---------- ----------
token = os.getenv("vfb_token")    

client.run(token)