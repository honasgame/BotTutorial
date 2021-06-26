import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  url = 'https://zenquotes.io/api/random'
  response = requests.get(url).json()
  return response

def build_quote():
  api_response = get_quote()
  quote = api_response[0]['q']
  author = api_response[0]['a']
  complete_quote = quote + ' -' + author
  return complete_quote

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
    "$help": "Available commands: [$hello, $howareyou, $favgames, $inspire_me]",
    "$inspire_me": build_quote()
  }

  if msg in request_response:
    await message.channel.send(request_response[msg]) 

my_secret = os.environ['TOKEN']
client.run(my_secret)