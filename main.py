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

def get_joke():
  url = 'https://v2.jokeapi.dev/joke/any'
  response = requests.get(url).json()
  return response

def build_joke():
  api_responce_3 = get_joke()
  joke_type = api_responce_3['category']
  actual_joke = api_responce_3['setup'] 
  and_joke = api_responce_3['delivery']
  complete_joke = joke_type + '-' + actual_joke + and_joke
  return complete_joke

def get_joke_programming():
  url = 'https://v2.jokeapi.dev/joke/Programming'
  response = requests.get(url).json()
  return response

def build_joke_programming():
  api_responce_4 = get_joke_programming()
  actual_joke = api_responce_4['setup'] 
  and_joke = api_responce_4['delivery']
  complete_joke = actual_joke + and_joke
  return complete_joke

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Game('?Use $help to get the list of commands'))
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
    "$help": "Available commands: [$hello: conversation, $howareyou: conversation, $favgames : conversation, $inspire_me: random inspirational quotes,$inspire_me_today: inspirational quote of the today,$joke:joke,$joke_programming: programming jokes]",
    "$inspire_me": build_quote(),
    "$inspire_me_today":build_quote_today(),
    "$joke":build_joke() ,
    "$joke_programming": build_joke_programming()
   
  }

  if msg in request_response:
    await message.channel.send(request_response[msg]) 

my_secret = os.environ['TOKEN']
client.run(my_secret)