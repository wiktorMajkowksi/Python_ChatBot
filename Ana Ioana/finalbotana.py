import asyncio
import discord
from googlesearch import search
import random
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.async_event
@asyncio.coroutine
def on_message(message):
        author = message.author
        if message.content.startswith('!welcome'):
                print('on_message !welcome')
                Greetings= ["`Hi`", "`Hey`", "`Hi there`", "`Hello`", "`I am glad! You are talking to me`"]
                yield from welcome(author, message)
                yield from message.channel.send(random.choice(Greetings))

        if message.content.startswith('!food'):
                print('on_message !food')
                yield from food(message)

        if message.content.startswith('!fastfood'):
                print('on_message !fastfood')
                yield from fastfood(message)

        if message.content.startswith('!restaurant'):
                print('on_message !restaurant')
                yield from restaurant(message)

        if message.content.startswith('!coventryfastfood'):
                print('on_message !coventry')
                Covfood= "Fastfood in Coventry"
                for url in search(Covfood, tld='com', lang='en', num=3, start=1, stop=2):
                        yield from message.channel.send(url)
        if  message.content.startswith('!birminghamfastfood'):
                print('on_message !birminghamfastfood')
                Birfood= "Fastfood in Birmingham"
                for url in search(Birfood, tld='com', lang='en', num=3, start=1, stop=2):
                        yield from message.channel.send(url)
        if  message.content.startswith('!londonfastfood'):
                print('on_message !londonfastfood')
                Lonfood= "Fastfood in London"
                for url in search(Lonfood, tld='com', lang='en', num=3, start=1, stop=2):
                        yield from message.channel.send(url)

        if message.content.startswith('!coventryrestaurant'):
                print('on_message !coventryrestaurant')
                CovRest= "Restaurants in Coventry"
                for url in search(CovRest, tld='com', lang='en', num=3, start=1, stop=2):
                        yield from message.channel.send(url)
        if  message.content.startswith('!birminghamrestaurant'):
                print('on_message !birminghamrestaurant')
                BirRest= "Restaurants in Birmingham"
                for url in search(BirRest, tld='com', lang='en', num=3, start=1, stop=2):
                        yield from message.channel.send(url)
        if  message.content.startswith('!londonrestaurant'):
                print('on_message !londonrestaurant')
                LonRest= "Restaurants in London"
                for url in search(LonRest, tld='com', lang='en', num=3, start=1, stop=2):
                        yield from message.channel.send(url)
         
        if message.content.upper() == "CS":
               cs_jokes = ("Why do programmers wear glasses? They can't C#",
               "How many programmers does it take to change a lightbulb? None, it's a hardware problem." ,
                           "To understand recursion one must first understand recursion.", "01010111011010000111100100100000011001000110100101100100001000000111010001101000011001010010000001100011011010000110100101100011011010110110010101101110001000000110001101110010011011110111001101110011001000000111010001101000011001010010000001110010011011110110000101100100001111110010000001010100010011110010000001000111010001010101010000100000010101000100111100100000010101000100100001000101001000000100111101010100010010000100010101010010001000000101001101001001010001000100010100100000010110010100000100100000010001000100100101010000010100110100100001001001010101000010000100100001",
                           "There are 10 types of people in the world - those who understand binary, and those who don't.",
                           "Real programmers count from 0.")
               yield from message.channel.send(random.choice(cs_jokes))

#run on my terminal for testing purpose
@client.event
async def on_ready():
  print('Logged in as:')
  print(client.user.name)
  print(client.user.id)
  

@asyncio.coroutine
def welcome(author, message):
        print('testing welcome')
        
def food(message):
        print('testing food')
        yield from message.channel.send('Please choose one : `!fastfood` & `!restaurant`')

def fastfood(message):
        print('testing fastfood')
        yield from message.channel.send('Please select the location where you want to eat: `!coventryfastfood`, `!birminghamfastfood`, `!londonfastfood`')

def restaurant(message):
        print('testing restaurant')
        yield from message.channel.send('Please select the location where you want to eat: `!coventryrestaurant`, `!birminghamrestaurant`, `!londonrestaurant`')


client.run("NTA2NjMwOTc4MDM5NTc4NjI0.DtTlRA.pn3Za5lLGFf_0fO6m7ImMIqBLew")

