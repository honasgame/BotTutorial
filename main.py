import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is ready! Command me')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content.lower()

  request_response = {
    "$hello": "Hello, this is the wild bot",
    "$howareyou": "I am fine thank you",
    "$favgames": "My three favourite games are cricket, football and badminton",
    "$help": "Available commands: [$hello, $howareyou, $favgames]" 
  }
  
  if msg.startswith('$hello'):

    await message.channel.send(request_response['$hello'])

  if msg.startswith('$howareyou'):
   
    await message.channel.send(request_response['$howareyou'])

  if msg.startswith('$favgames'):
 
    await message.channel.send(request_response['$favgames'])
  if msg.startswith('$help'):

    await message.channel.send(request_response['$help'])



my_secret = os.environ['TOKEN']
client.run(my_secret)