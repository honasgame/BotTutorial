import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  url = 'https://zenquotes.io/api/random'
  response = requests.get(url).json()
  return response

def get_quote_today():
  url = 'https://zenquotes.io/api/today'
  response_2 = requests.get(url).json()
  return response_2

def build_quote():
  api_response = get_quote()
  quote = api_response[0]['q']
  author = api_response[0]['a']
  complete_quote = quote + ' -' + author
  return complete_quote
  
def build_quote_today():
  api_response_2 = get_quote_today()
  quote_2 = api_response_2[0]['q']
  author_2 = api_response_2[0]['a']
  complete_quote_2 = quote_2 + ' -' + author_2
  return complete_quote_2

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
    "$help": "Available commands: [$hello: conversation, $howareyou: conversation, $favgames : conversation, $inspire_me: random inspirational quotes,$inspire_me_today: inspirational quote of the today]",
    "$inspire_me": build_quote(),
    "$inspire_me_today":build_quote_today()
  }

  if msg in request_response:
    await message.channel.send(request_response[msg]) 

my_secret = os.environ['TOKEN']
client.run(my_secret)