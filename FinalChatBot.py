import asyncio
import json
import re
import urllib.request
import webbrowser
import aiohttp
import requests

#####       ANA imports       ########
import discord
#from googlesearch import search
import random

#########################################

######                  IOANA imports                   ############

import time
import urllib
import datetime as dt

reminder=0

######################


###########         Nefeli imports            #################

from random import shuffle , randint

###############################


"""Those import the functions from python standard library"""
from discord import Game
from discord.ext.commands import Bot

##########Bot prefix assignment##########

BOT_PREFIX = ""

client = Bot(command_prefix=BOT_PREFIX)

##########Main Code Body##########

@client.command(aliases = ['hey','Hello','hi','Hey','Hi','HEY','HI','HELLO']) # Aliases enable this command to be triggered in different ways.
async def hello():
    await client.say("Hello!")

@client.command(aliases = ["sweets", "Dessert"])
async def dessert():
    await client.say("What would you like to eat for your desert?"          #This line asks the user which option they want to choose
                     "\n"
                     "\n" "I can offer you the following:"
                     "\n" "1)  Ice-cream: £2 (add an extra scoop for 50p)."
                     "\n" "2)  Cake: £3 per slice."
                     "\n" "3)  Fruits: £1 per bowl.")
    """Those print commands create a welcome interface"""

    @client.command(aliases= ['ice-cream', 'IceCream', '1'])
    async def ice_cream():
        await client.say("What ice-cream flavour would you like?"
                         "\n"
                         "\n" "a) Chocolate"
                         "\n" "b) Strawberry"
                         "\n" "c) Lemon"
                         "\n" "d) Toffi"
                         "\n" "e) Vanilla")

    @client.command(aliases=['Cake', 'CAKE', '2'])
    async def cake():
        await client.say("What cake flavour would you like?"
                         "\n"
                         "\n" "a) Carrot cake"
                         "\n" "b) Chocolate cake"
                         "\n" "c) Caramel cake")

    @client.command(aliases=['Fruits', 'fruit', '3'])
    async def fruits():
        await client.say("What fruits would you like"
                         "\n"
                         "\n" "a) Strawberries"
                         "\n" "b) Blackcurrants"
                         "\n" "c) Blueberries"
                         "\n" "d) Oranges")

@client.command()   #This code I obtained from this website ---> https://www.devdungeon.com/content/make-discord-bot-python-part-2
async def bitcoin():        #(It is the code that helped me to understand how to use API's)
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.command()   #This code will show weather forecast for tomorrow
async def weather():
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=487189a4845348a2844131423181211&q=London&format=json&num_of_days=1"    #This is a weather API that I found
    output1 = requests.get(url) #This requests and gets the API link above
    ans = output1.json()['data']['weather'][0]['hourly'][7]['tempC']    #This filters through the API in order to get the information that is required
    await client.say("The temperature tomorrow in London will be:  %s °C" % ans)

@client.command()    #This code conducts a google search
async def google(a):
    url = "https://www.google.com/search?ei=EMjyW7G-NMaagQbP2qmYCw&q={}".format(a)
    new = 2
    webbrowser.open(url, new=new)
    await client.say("This is link might be useful for query: " + url)

@client.command(aliases= ["nav", "Nav", "NAV", ])   #This code is the navigation code
async def where_c(o, d):
    endpoint = "https://maps.googleapis.com/maps/api/directions/json?"  # This is the base of the link that api we need will be build on
    key = "AIzaSyCjxBL-51EMWIs35JegWcQ8Q5Y8MmpA_ww"
    nav_request = "origin={}&destination={}&key={}".format(o, d, key)  # Here I have formated the origin, destination and the key using the variables that I have created above.
    request = endpoint + nav_request
    print(request)
    response = urllib.request.urlopen(request).read()  # This line uses a urllib.request to read the Api that we have requested.
    str_response = response.decode('utf-8')  # This line is responsible for decoding the data from the Api
    directions = json.loads(str_response)
    routes = directions["routes"]
    legs = routes[0]["legs"]
    legs2 = legs[0]["steps"]
    a = len(legs2) - 1
    x = 0
    if a >= x:
        while a >= x:
            c = legs[0]["steps"][x]["distance"]["text"]
            b = legs[0]["steps"][x]["html_instructions"]
            endSTR = (str(x + 1) + ") " + (re.sub("<b>|</b>|</div>|<div|style=\"font-size:0.9em\">", "", b)) + ". For: " + c) # re.sub allows me to remove more than one character from the string
            await client.say(endSTR)
            x = x + 1
    #finally:
     #       await client.say("Sorry I don't know those locations. Try different ones, maybe I will be able to help with them.")

@client.event
async def on_ready():
    await client.change_presence(game=Game (name="with You!"))
    print("Logged in as " + client.user.name)

@asyncio.coroutine
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:     #this is code is ran when the user is not active
        print("Current servers: general")
        for server in client.servers:
            print(server.name)
            await asyncio.sleep(100)    #This code prints the server that the bot is on recursively until the user interacts with chatbot.


#######         ANA CODE            #######

@client.event
@asyncio.coroutine
async def on_message(message):
    author = message.author
    if message.content.startswith('!welcome'):
        print('on_message !welcome')
        Greetings = ["`Hi`", "`Hey`", "`Hi there`", "`Hello`", "`I am glad! You are talking to me`"]
        await welcome(author, message)
        await message.channel.send(random.choice(Greetings))

    if message.content.startswith('!food'):
        print('on_message !food')
        await food(message)

    if message.content.startswith('!fastfood'):
        print('on_message !fastfood')
        await fastfood(message)

    if message.content.startswith('!restaurant'):
        print('on_message !restaurant')
        await restaurant(message)

    if message.content.startswith('!coventryfastfood'):
        print('on_message !coventry')
        Covfood = "Fastfood in Coventry"
        for url in search(Covfood, tld='com', lang='en', num=3, start=1, stop=2):
            await message.channel.send(url)
    if message.content.startswith('!birminghamfastfood'):
        print('on_message !birminghamfastfood')
        Birfood = "Fastfood in Birmingham"
        for url in search(Birfood, tld='com', lang='en', num=3, start=1, stop=2):
            await message.channel.send(url)
    if message.content.startswith('!londonfastfood'):
        print('on_message !londonfastfood')
        Lonfood = "Fastfood in London"
        for url in search(Lonfood, tld='com', lang='en', num=3, start=1, stop=2):
            await message.channel.send(url)

    if message.content.startswith('!coventryrestaurant'):
        print('on_message !coventryrestaurant')
        CovRest = "Restaurants in Coventry"
        for url in search(CovRest, tld='com', lang='en', num=3, start=1, stop=2):
            await message.channel.send(url)
    if message.content.startswith('!birminghamrestaurant'):
        print('on_message !birminghamrestaurant')
        BirRest = "Restaurants in Birmingham"
        for url in search(BirRest, tld='com', lang='en', num=3, start=1, stop=2):
            await message.channel.send(url)
    if message.content.startswith('!londonrestaurant'):
        print('on_message !londonrestaurant')
        LonRest = "Restaurants in London"
        for url in search(LonRest, tld='com', lang='en', num=3, start=1, stop=2):
            await message.channel.send(url)

    if message.content.upper() == "CS":
        cs_jokes = ("Why do programmers wear glasses? They can't C#",
                    "How many programmers does it take to change a lightbulb? None, it's a hardware problem.",
                    "To understand recursion one must first understand recursion.",
                    "01010111011010000111100100100000011001000110100101100100001000000111010001101000011001010010000001100011011010000110100101100011011010110110010101101110001000000110001101110010011011110111001101110011001000000111010001101000011001010010000001110010011011110110000101100100001111110010000001010100010011110010000001000111010001010101010000100000010101000100111100100000010101000100100001000101001000000100111101010100010010000100010101010010001000000101001101001001010001000100010100100000010110010100000100100000010001000100100101010000010100110100100001001001010101000010000100100001",
                    "There are 10 types of people in the world - those who understand binary, and those who don't.",
                    "Real programmers count from 0.")
        await message.channel.send(random.choice(cs_jokes))
    await client.process_commands(message)

# run on my terminal for testing purpose
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
    yield from message.channel.send(
        'Please select the location where you want to eat: `!coventryfastfood`, `!birminghamfastfood`, `!londonfastfood`')


def restaurant(message):
    print('testing restaurant')
    yield from message.channel.send(
        'Please select the location where you want to eat: `!coventryrestaurant`, `!birminghamrestaurant`, `!londonrestaurant`')

#######################################################################

###########         IOANA CODE              ####################

commandList = ["!date", "!time", "!say", "!google", "!help", "!rating", "!news"]
newsCategories = ["!business", "!sports", "!entertainment", "!general", "!health", "!science", "!technology"]
thanks_list = ['thank', 'thanks', 'thx']


async def news_category(cat):
    category = str(cat)
    url = (
                'https://newsapi.org/v2/top-headlines?country=gb&category=' + category + '&apiKey=3b0e65b114564b8d8e5382fbddfc2df5')
    return url


async def news_keyword(word):
    keyword = str(word)
    word = keyword[1:]
    url = ('https://newsapi.org/v2/top-headlines?q=' + word + '&apiKey=3b0e65b114564b8d8e5382fbddfc2df5')
    return url


async def news_search(url):
    # response = requests.get(url)
    # print (response.json())
    response = urllib.request.urlopen(url).read()
    replyjson = str(response, 'utf-8')
    read = json.loads(replyjson)

    if len(read["articles"]) == 0:
        print('ERROR')

        return "__`Sorry, there are no articles containing this word.`__"

    source1 = read["articles"][0]["source"]['name']
    title1 = read["articles"][0]["title"]
    description1 = read["articles"][0]["description"]
    url1 = read["articles"][0]["url"]

    source2 = read["articles"][1]["source"]['name']
    title2 = read["articles"][1]["title"]
    description2 = read["articles"][1]["description"]
    url2 = read["articles"][1]["url"]

    source3 = read["articles"][2]["source"]['name']
    title3 = read["articles"][2]["title"]
    description3 = read["articles"][2]["description"]
    url3 = read["articles"][2]["url"]

    return source1, title1, description1, url1, source2, title2, description2, url2, source3, title3, description3, url3


@client.event
async def on_message(message):
    contents = message.content.split(" ")
    if message.author == client.user:
        return

    # ------Looking for commands---------------------------------------------------"""

    if message.content.startswith('!'):
        if message.content in commandList or message.content in newsCategories or '!google' in message.content or '!say' in message.content:
            pass
        else:
            await client.send_message(message.channel,
                                      "__`Sorry, I didn't catch that. For things I can help you with, type '!help'.`__")

    # -------------------------------------------------------------------------------"""
    # --------Google ----------------------------------------------------------------"""
    # This is the module used for the code below:
    # https://pypi.org/project/beautifulsoup4/
    # And also, this code is not written by me

    if message.content.lower().startswith("!google"):
        url = message.content.lower()
        url = url[8:]

        reply = ":small_blue_diamond:Here are the top three results for your search {0.author.mention}:".format(message)
        await client.send_message(message.channel, reply)

        for search1 in search(url, tld="com", num=3, stop=1, pause=2):
            await client.send_message(message.channel, "<" + search1 + ">")

    # -----------------------------------------------------------------------------"""
    # -----Date&Time---------------------------------------------------------------"""
    # To understand how to work with time in python I used this:
    # https://www.techatbloomberg.com/blog/work-dates-time-python/

    if message.content == '!time':
        url = "http://worldtimeapi.org/api/timezone/Europe/London.txt"
        datetime = dt.datetime.now().isoformat()
        reply = datetime[11:16]
        await client.send_message(message.channel, ':small_blue_diamond: `Here is the time: ' + reply + '`')

    if message.content == '!date':
        datetime = dt.datetime.now().isoformat()
        day = datetime[8:10]
        month = datetime[5:7]
        year = datetime[0:4]
        await client.send_message(message.channel, ':small_blue_diamond: `Day: ' + day + '`')
        await client.send_message(message.channel, ':small_blue_diamond: `Month: ' + month + '`')
        await client.send_message(message.channel, ':small_blue_diamond: `Year: ' + year + '`')

    # -----End of Date&Time-------------------------------------------------------"""

    if message.content == "!help":
        reply1 = "Hello {0.author.mention}".format(message)
        reply2 = "This are the commands that you can use at the moment(most of them are self explanatory):"
        reply3 = ":small_blue_diamond: Use '?google' for a quick google search."
        reply4 = ":small_blue_diamond: Use '?rating' to get a chance to rate me. "
        reply5 = ":small_blue_diamond: Use '?news' to find out the top three articles today about the topic of your choice. "
        reply6 = ":small_blue_diamond: Use '?date' to find out the date."
        reply7 = ":small_blue_diamond: Use '?time' to find out the time. "
        reply8 = ":small_blue_diamond: Use '?say' to make me say something. "

        await client.send_message(message.channel,
                                  reply1 + '\n' + reply2 + '\n' + reply3 + '\n' + reply4 + '\n' + reply5 + '\n' + reply6 + '\n' + reply7 + '\n' + reply8)

    # ---------News api-------------------------------------------------------"""
    # https://newsapi.org/docs/get-started
    # This is the website that I used to get the API
    # I also used it to understand how do the parameters work
    # (For example, the country, the keyword, which is noted by 'q', and also the category)
    # This information can be found here: https://newsapi.org/docs/endpoints/top-headlines

    if message.content == '!news':
        reply1 = "Please choose a category: business, sports, entertainment, general, science, health, technology."
        reply2 = "Don't forget to use '!' before."
        reply3 = "If you're searching for a specific topic, then just type '!' and then your keyword. "
        await client.send_message(message.channel,
                                  '`' + reply1 + '\n' + reply2 + '`' + ':blush:' + '\n' + '`' + reply3 + '`')

    if message.content in newsCategories:
        presentation = "Here are the top three news articles in the category that you selected, {0.author.mention}.".format(
            message)
        cat = str(message.content)
        category = cat[1:]
        list_news = list(await news_search(await news_category(category)))

        try:

            source1 = list_news[0]
            title1 = list_news[1]
            description1 = list_news[2]
            link1 = list_news[3]

            source2 = list_news[4]
            title2 = list_news[5]
            description2 = list_news[6]
            link2 = list_news[7]

            source3 = list_news[8]
            title3 = list_news[9]
            description3 = list_news[10]
            link3 = list_news[11]

            await client.send_message(message.channel,
                                      presentation + '\n' + ':small_blue_diamond: Number 1:' + '\n' + 'Source: ' + source1 + '\n' + 'Title: ' + title1 + '\n' + 'Description: ' + description1 + '\n' + '<' + link1 + '>' + '\n' + ':small_blue_diamond: Number 2: ' + '\n' + 'Source: ' + source2 + '\n' + 'Title: ' + title2 + '\n' + 'Description: ' + description2 + '\n' + '<' + link2 + '>' + '\n' + ':small_blue_diamond: Number3: ' + '\n' + 'Source: ' + source3 + '\n' + 'Title: ' + title3 + '\n' + 'Description: ' + description3 + '\n' + '<' + link3 + '>')


        except:
            await client.send_message(message.channel,
                                      'Sorry there are not enough articles in that category. You can try another one if you want, {0.author.mention}.'.format(
                                          message))

    if message.content.startswith('!'):
        presentation = "Here are the first three articles containing the keyword that you entered,  {0.author.mention}.".format(
            message)
        mes = str(message.content)
        keyword = mes[1:]
        list_news = list(await news_search(await news_keyword(keyword)))

        if len(list_news) == 12:
            source1 = list_news[0]
            title1 = list_news[1]
            description1 = list_news[2]
            link1 = list_news[3]

            source2 = list_news[4]
            title2 = list_news[5]
            description2 = list_news[6]
            link2 = list_news[7]

            source3 = list_news[8]
            title3 = list_news[9]
            description3 = list_news[10]
            link3 = list_news[11]

            await client.send_message(message.channel,
                                      presentation + "\n" + ":small_blue_diamond: Number 1:" + "\n" + "Source: " + source1 + "\n" + "Title: " + title1 + "\n" + "Description: " + description1 + "\n" + "<" + link1 + ">" + "\n" + ":small_blue_diamond: Number 2:" + "\n" + "Source: " + source2 + "\n" + "Title: " + title2 + "\n" + "Description: " + description2 + "\n" + "<" + link2 + ">" + "\n" + ":small_blue_diamond: Number 3:" + "\n" + "Source: " + source3 + "\n" + "Title: " + title3 + "\n" + "Description: " + description3 + "\n" + "<" + link3 + ">")



        else:
            await client.send_message(message.channel, await news_search(await news_keyword(keyword)))

    # ----------------------------------------------------------------------------------"""

    if message.content.upper().startswith("WHAT'S YOUR NAME?") or message.content.upper().startswith(
            "WHATS YOUR NAME") or message.content.upper().startswith("WHAT'S YOUR NAME"):
        reply = "My name is Dave. It is a pleasure to meet you {0.author.mention}. :grinning:".format(message)
        await client.send_message(message.channel, reply)

    if message.content.upper().startswith('?SAY'):
        m1 = message.content.split(" ")
        await client.send_message(message.channel, '`' + (" ".join(m1[1:])) + '`')

    if message.content.upper().startswith('AWE') or message.content.upper().startswith(
            'AW') or message.content.upper().startswith("AWW"):
        reply = ["awe",
                 ":heart_eyes:"]
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper().startswith('HI') or message.content.upper().startswith(
            'HELLO') or message.content.upper().startswith('HEY') or message.content.upper().startswith('HEYY'):
        reply = "Hello there {0.author.mention} and welcome to my server. Don't forget to use the prefix '?' for commands.".format(
            message)
        await client.send_message(message.channel, reply)

    if message.content.upper().startswith("HOW ARE YOU?") or message.content.upper().startswith(
            "HOW ARE YOU") or message.content.upper().startswith("HOW ARE U") or message.content.upper().startswith(
            "HOW'S IT GOING?") or message.content.upper().startswith("HOW'S IT GOING"):
        reply = ["Much better now that you are with me.",
                 "Do you really care?",
                 "Like you, but better.",
                 "Can't complain. Nobody listens to me anyway.",
                 "Yes",
                 "My psychiatrist told me not to discuss it with strangers.",
                 "Next question, please.",
                 "Your attempt at social interaction is hereby acknowledged.",
                 "I promised myself I would kill the next person who asked me that question, but I like you so I will let you live.",
                 "I'd be better if you asked me out.",
                 "Just hug me and leave it at that.",
                 "What do you think is the worst way to die?"]

        await client.send_message(message.channel, '`' + random.choice(reply) + '`')

    if message.content.upper().startswith("YOU'RE BEAUTIFUL") or message.content.upper().startswith(
            "YOU ARE BEAUTIFUL") or message.content.upper().startswith(
            "YOU'RE SO HANDSOME") or message.content.upper().startswith(
            "YOU ARE PRETTY") or message.content.upper().startswith("YOU'RE PRETTY"):
        reply = ["You must be looking at a mirror.",
                 "Is that the best you’ve got?",
                 "Look who’s talking.",
                 "Well, that makes two of us!",
                 "Thanks, but I prefer to be noticed for my intellectual capacity.",
                 "Yeah, it’s my only redeeming quality.",
                 "Not this again...take a number and wait in line.",
                 "It’s extremely rare for me to hear that.",
                 "Oh stop it, you.",
                 "Awww...now I want to throw a rainbow at you.",
                 "What do you need?",
                 "Compliment accepted.",
                 "It must be the meds kicking in.",
                 "I know. Wish I could say the same about you.",
                 "Thanks, wanna get a room?"]
        await client.send_message(message.channel, random.choice(reply))
        await client.send_file(message.channel, 'robot.photo.jpg')

    for word in contents:
        if word in thanks_list:
            reply = ["I'm happy to help.",
                     "You got it.",
                     "My pleasure.",
                     "Anytime.",
                     "No worries.",
                     "Don't mention it."]
            await client.send_message(message.channel, '`' + random.choice(reply) + '`')

    if message.content.upper().startswith("WHAT IS THE MEANING OF LIFE") or message.content.upper().startswith(
            "WHAT'S THE MEANING OF LIFE?") or message.content.upper().startswith(
            "WHAT'S THE MEANING OF LIFE") or message.content.upper().startswith("WHAT IS THE MEANING OF LIFE?"):
        reply = ["To die.",
                 "I don't think there is one. I think it's all just a series of incredible, beautiful, and meaningless coincidences, which we might as well enjoy.",
                 "I give up.",
                 "42", ]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')

    if message.content.upper().startswith("HAHA") or message.content.upper().startswith(
            "HAH") or message.content.upper().startswith("HAHAH") or message.content == "ha":
        reply = ["I'm happy I made you laugh",
                 ":joy: :joy: :joy:",
                 ":wink:",
                 ":sweat_drops: :sweat_drops: :peach:"]
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper().startswith("DAVE?") or message.content.upper().startswith(
            "DAVE") or message.content.upper().startswith("DAV") or message.content.upper().startswith("DAV?"):
        reply = ["Yes?",
                 "Right here."
                 "How may I help you?",
                 "Oh, you again.",
                 "Still here."]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')

    if message.content.upper().startswith("BYE") or message.content.upper().startswith(
            "GOODBYE") or message.content.upper().startswith("GOODNIGHT"):
        reply = ["Bye bye",
                 "See you next time!",
                 "Take care.",
                 "Hav a nice day!",
                 "I'll be right here waiting for you."]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')

    if message.content.upper().startswith('?RATING'):
        msg = await client.send_message(message.channel,
                                        '`Let me know what you think about me. React with thumbs up or thumbs down.`')
        res = await client.wait_for_reaction(['👍', '👎'], message=msg)
        await client.send_message(message.channel,
                                  '`{0.user} thank you for your reaction {0.reaction.emoji}!`'.format(res))

    if message.content.endswith('?'):
        reply = ["Signs point to yes.",
                 "Without a doubt.",
                 "As I see it, yes.",
                 "Better not tell you now.",
                 "Most likely.",
                 "My reply is no.",
                 "Don't count on it.",
                 "No."]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')

    if message.content.upper().startswith("LET'S") or message.content.upper().startswith("LETS"):
        reply = ["Hell no",
                 "Hell yes",
                 "I'm down"]
        await client.send_message(message.channel, random.choice(reply))
    await client.process_commands(message)

########################################################################

##########          NEFELI CODE           ######################

a = ['WEATHER' , 'WHAT' , 'HOW']

#First API for google wikipedia
#this function is for the API for wikipedia google search
def google (input):
    url = 'https://en.wikipedia.org/wiki'
    search_string = '/'
    use_word = input
    final1_string = url + search_string + use_word
    return final1_string

#this comand uses the funcion above and it's suppose to give to the user the information for the the word that the user types
@client.command()
async def google_sea(arg):
    use_word = arg
    location = arg
    string22 =  'There is your result about ' + location + ' '
    try:
        var1 = google(use_word)
        finast = string22 + str(var1)
        await client.say(finast)
    except:
        await client.say("error!Type again")

#Combination of the two API's
#the command below it takes the user's input and output the temperature of the town or city that the user types and also some extra inforamtion about the input
@client.command()
async def google_temp(arg):
    use_word = arg
    location = arg
    string22 =  'Also some information about ' + location + ' '
    try:
        var1 = google(use_word)
        finast = string22 + str(var1)
        var3 = temp_url(location)
        var4 = current_weather(var3)
        string2 = str('The temperature in ' + location + ' is ' + str(var4))

        await client.say(string2)
        await client.say(finast)

    except:
        await client.say("error!Type again")

#the command below gives to the user the temperature in Fahrenheit and also some extra information for the user's input
@client.command()
async def google_tempf(arg):
    use_word = arg
    location = arg
    string22 = 'Also some information about ' + location + ' '
    try:
        var1 = google(use_word)
        finast = string22 + str(var1)
        var3 = temp_url(location)
        var4 = tempf(var3)
        string2 = str('The temperature in Fahrenheit in ' + location + ' is ' + str(var4))

        await client.say(string2)
        await client.say(finast)

    except:
        await client.say("error!Type again")


#The command below gives the uv index and also some information for the user's input
@client.command()
async def google_uv(arg):
    use_word = arg
    location = arg
    string22 = 'Also some information about ' + location + ' '
    try:
        var1 = google(use_word)
        finast = string22 + str(var1)
        var3 = temp_url(location)
        var4 =uv_index_func(var3)
        var5 = uv_warning(var4)
        string2 = str('The uv index in ' + location + ' is ' + str(var4) + str(var5))

        await client.say(string2)
        await client.say(finast)
    except:
        await client.say("error!Type again")


#the command below gives to the user the wind  and also some information about the user's input
@client.command()
async def google_wind(arg):
    use_word = arg
    location = arg
    string22 = 'Also some information about ' + location + ' '
    try:
        var1 = google(use_word)
        finast = string22 + str(var1)
        var3 = temp_url(location)
        var4 =wind_di(var3)
        string2 = str('The wind in ' + location + ' is ' + str(var4) )

        await client.say(string2)
        await client.say(finast)
    except:
        await client.say("error!Type again")







#second API
#the function below it is suppose to take the the city/town that the user input's and gives the main url that the information will come from so that the bot can show
def temp_url(input: object) -> object:
    main_url = 'http://api.apixu.com/v1/current.json'
    api_key = '?key=dc42d220696a4172b65174631181611'
    search_string = '&q='
    location = input
    final_string = main_url + api_key + search_string + location
    return final_string

#This function gives you the proper messages if the uv index is hight how you can protect yourself
#It takes the input and with an if statement it sees how hight is it and prints the message
def uv_warning(arg):
    values = ' '
    UV_index = arg
    uv3 = 'You need sunglasses'
    uv5 = uv3 + ' and a hat and you need to stay in shade'
    uv11 = uv5 + '. Stay indoors between 10am - 4am'
    if UV_index >= 3 and UV_index < 5:
        values = uv3
    if UV_index >= 5 and UV_index < 11:
        values = uv5
    if UV_index >= 11:
        values = uv11
    return values
@client.command()
async def uv(arg):
    location = arg
    string22 = 'The UV index in ' + location + " is "

    #in this part of the function the 'var1' takes the ciy name and puts it in the url
    #after the 'var2' calls the function 'uv_index_func' with input the 'var1' so that it can collects the proper information from the url to print it to the user
    #the same is happening for the above 'async' functions
    try:
        var1 = temp_url(location)
        var2 = uv_index_func(var1)
        var3 = uv_warning(var2)
        final_string = string22 + str(var2) + var3
        await client.say(final_string)
    except:
        await client.say("This city doesn't exist!Try again")

#the two functions below they take the city/town/country that the user input and they take from the API dictionary the exact information that we want
def current_weather(input):
    url = input
    response = urllib.request.urlopen(url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)
    #if you want the entire dictonary
    #final = data
    final = (data['current']['temp_c'])
    return final
def uv_index_func(input):
    url = input
    response = urllib.request.urlopen(url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)
    #if you want the entire dictonary
    #final = data
    final = (data['current']['uv'])
    return final

#gives the temperature of the location that the user want's
@client.command()
async def temp(arg):
    location = arg
    string22 = 'The temperature in ' + location + " is "
    try:
        var1 = temp_url(location)
        var2 = current_weather(var1)
        final_string = string22 + str(var2)
        await client.say(final_string)
   #if the location that the user input does not exist it will come up with an error
    except:
        await client.say("This city doesn't exist!Try again")



#gives the temperature in Fahrenheit of the location that the user want's
@client.command()
async def ftemp(arg):
    location = arg
    string22 = 'The temperature in Fahrenheit in ' + location + " is "
    try:
        var1 = temp_url(location)
        var2 = tempf(var1)
        final_string = string22 + str(var2)
        await client.say(final_string)
    # if the location that the user input does not exist it will come up with an error
    except:
        await client.say("This city doesn't exist!Try again")



def tempf(input):
    url = input
    responce = urllib.request.urlopen(url).read()
    json_obj = str(responce,'utf-8')
    data = json.loads(json_obj)
    final = (data['current']['temp_f'])
    return final



#gives the wind of the location that the user want's
@client.command()
async def wind(arg):
    location = arg
    string22 = 'The wind in ' + location +  " is "
    try:
        var1 = temp_url(location)
        var2 = wind_di(var1)
        final_string = string22 + str(var2)
        await client.say(final_string)
    except:
        await client.say("This city doesn't exist!Try again")

def wind_di(input):
    url= input
    responce = urllib.request.urlopen(url).read()
    json_obj = str(responce, 'utf-8')
    data = json.loads(json_obj)
    final = (data['current']['wind_mph'])
    return final


########################################################################

client.loop.create_task(list_servers())
client.run("NTA2NDkxOTY5Njg2NDcwNjU3.Dr4Lvw.mJ0_I5DHwbr5fMzDaZt9SHuzT1k")