import json
import re
import urllib.request

"""Those import the functions from python standard library"""
from discord.ext.commands import Bot

##########Bot prefix assignment##########

BOT_PREFIX = ""

client = Bot(command_prefix=BOT_PREFIX)

########## Main code ##########

@client.event
async def on_message(message):
    await client.process_commands(message)
    endpoint = "https://maps.googleapis.com/maps/api/directions/json?"  # This is the base of the link that api we need will be build on
    key = "AIzaSyCjxBL-51EMWIs35JegWcQ8Q5Y8MmpA_ww"

    origin = "London" #("Where are you?: ").replace(" ", "+")
    destination = "Bedworth" #("Where do you want to go?: ").replace(" ", "+")
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
    if a>=x:
        while a >= x:
            #timeForJourney = legs[0]["duration"]["text"]
            c = legs[0]["steps"][x]["distance"]["text"]
            b = legs[0]["steps"][x]["html_instructions"]
            summer = (str(x + 1) + ") " + (re.sub("<b>|</b>|</div>|<div|style=\"font-size:0.9em\">", "",b)) + ". For: " + c)
            # re.sub allows me to remove more than one character from the string
            if message.content.startswith("message"):
                await client.send_message(message.channel, summer)
            x = x + 1
            #if message.content.startswith(""):
                #await client.send_message(message.channel, ("The estimated time for your journey is: " + timeForJourney))
    else:
        await client.say("I didn't catch that, could you repeat?")
