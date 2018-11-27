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
         
        if message.content.upper() == "YM":
               yo_momma = ("fat, I took a picture of her last Christmas and it's still printing.",
               "fat when she got on the scale it said, 'I need your weight not your phone number.'",
               "fat and old when God said, 'Let there be light', he asked your mother to move out of the way.",
               "fat she doesn't need the internet, because she's already world wide.",
               "fat, when she sat on an iPod, she made the iPad!",
               "fat she walked past the TV and I missed 3 episodes.",
               "ugly when she tried to join an ugly contest they said, 'Sorry, no professionals.'",
               "ugly she made One Direction go another direction.",
               "ugly Fix-It Felix said, 'I can\'t fix it.'"
               "stupid when an intruder broke into her house, she ran downstairs, dialed 9-1-1 on the microwave, and couldn't find the 'CALL' button.",
               "stupid she stuck a battery up her ass and said, 'I GOT THE POWER!'",
               "stupid that she sat on the TV to watch the couch.")
               yield from message.channel.send("Yo momma so {}".format(random.choice(yo_momma)))

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

