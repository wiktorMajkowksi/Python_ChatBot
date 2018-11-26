import asyncio
import json
import re
import urllib.request
import webbrowser
import aiohttp
import requests

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

@client.command(aliases = ["sweets", "Dessert"])  #Works
async def dessert():
    await client.say("What would you like to eat for your desert?"
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

@client.command()   #Works (not mine)
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.command()   #Works
async def weather():
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=487189a4845348a2844131423181211&q=London&format=json&num_of_days=1"
    output1 = requests.get(url)
    ans = output1.json()['data']['weather'][0]['hourly'][7]['tempC']
    await client.say("The temperature tomorrow in London will be:  %s °C" % ans)

@client.command()    #Works (partly)
async def google():
    url = "https://www.google.com/search?ei=EMjyW7G-NMaagQbP2qmYCw&q={}".format(input)
    new = 2
    webbrowser.open(url, new=new)
    await client.say(url)

@client.command(aliases= ["nav", "Nav", "NAV", ])
async def where_c(o, d):
    endpoint = "https://maps.googleapis.com/maps/api/directions/json?"  # This is the base of the link that api we need will be build on
    key = "AIzaSyCjxBL-51EMWIs35JegWcQ8Q5Y8MmpA_ww"
    origin =  o.replace(" ", "+")
    destination = d.replace(" ", "+")
    nav_request = "origin={}&destination={}&key={}".format(origin, destination, key)  # Here I have formated the origin, destination and the key using the variables that I have created above.
    request = endpoint + nav_request
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
            timeForJourney = legs[0]["duration"]["text"]
            c = legs[0]["steps"][x]["distance"]["text"]
            b = legs[0]["steps"][x]["html_instructions"]
            endSTR = (str(x + 1) + ") " + (re.sub("<b>|</b>|</div>|<div|style=\"font-size:0.9em\">", "", b)) + ". For: " + c) # re.sub allows me to remove more than one character from the string
            await client.say(endSTR)
            x = x + 1
            if x == legs[0]["steps"]:
                await client.say("The estimated time for your journey is: " + timeForJourney)
    else:
        await client.say("I didn't catch that, could you repeat?")

@client.event
async def on_ready():
    await client.change_presence(game=Game (name="You"))
    print("Logged in as " + client.user.name)

@asyncio.coroutine
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers: general")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(100)
client.loop.create_task(list_servers())
client.run("NTA2NDkxOTY5Njg2NDcwNjU3.Dr4Lvw.mJ0_I5DHwbr5fMzDaZt9SHuzT1k")