import urllib.request
import json
import re
#api_key for google maps  == AIzaSyCjxBL-51EMWIs35JegWcQ8Q5Y8MmpA_ww  ##This is an API key that is requiered to access the Google Maps Api.
                                                                       #The key is unique and should be kept private for security reason.

#This code was writen according to the tutorial guide that can be found here --> https://www.youtube.com/watch?v=UrrWxyq1Z48
def googleMaps():
    endpoint = "https://maps.googleapis.com/maps/api/directions/json?" #This is the base of the link that api we need will be build on
    key = "AIzaSyCjxBL-51EMWIs35JegWcQ8Q5Y8MmpA_ww"
    origin = input("Where are you?: ").replace(" ","+")
    destination = input("Where do you want to go?: ").replace(" ","+")
    nav_request = "origin={}&destination={}&key={}".format(origin, destination, key) #Here I have formated the origin, destination and the key using the variables that I have created above.
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read() #This line uses a urllib.request to read the Api that we have requested.
    str_response = response.decode('utf-8') #This line is responsible for decoding the data from the Api
    directions = json.loads(str_response)
    routes = directions["routes"]
    legs = routes[0]["legs"]
    legs2 = legs[0]["steps"]
    a = len(legs2)-1
    x = 0
    while a >= x:
        timeForJourney = legs[0]["duration"]["text"]
        c = legs[0]["steps"][x]["distance"]["text"]
        b = legs[0]["steps"][x]["html_instructions"]
        print(str(x+1) + ") " + (re.sub("<b>|</b>|</div>|<div|style=\"font-size:0.9em\">", "", b)) + ". For: " +  c) #re.sub allows me to remove more than one character from the string
        x = x + 1
    print("The estimated time for your journey is: " + timeForJourney)
    #print(request)
    #print(len(legs2))
googleMaps()

#London

#Heathrow Airport

#n=number of steps


