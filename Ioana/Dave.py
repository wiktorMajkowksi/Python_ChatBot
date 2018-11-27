import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import aiohttp
import time
import random
import json
import urllib
import requests
import datetime as dt
from googlesearch import search



Client=discord.Client()
client=commands.Bot(command_prefix='?')
reminder=0

@client.event
async def on_ready():
    print('Bot is ready')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = " with fire "))


commandList=["?date", "?time", "?say", "?google", "?help", "?rating", "?news"]
newsCategories=["?business", "?sports", "?entertainment", "?general", "?health", "?science", "?technology"]
thanks_list=['thank','thanks','thx']    
   

async def news_category(cat):
    category=str(cat)
    url=('https://newsapi.org/v2/top-headlines?country=gb&category=' + category + '&apiKey=3b0e65b114564b8d8e5382fbddfc2df5')
    return url

async def news_keyword(word):
    keyword=str(word)
    word=keyword[1:]
    url=('https://newsapi.org/v2/top-headlines?q=' + word + '&apiKey=3b0e65b114564b8d8e5382fbddfc2df5')
    return url


async def news_search(url):
    #response = requests.get(url)
    #print (response.json())
    response=urllib.request.urlopen(url).read()
    replyjson=str(response, 'utf-8')
    read=json.loads(replyjson)
    
    if len(read["articles"]) == 0:
        print('ERROR')
        
        return "__`Sorry, there are no articles containing this word.`__"
    
    source1=read["articles"][0]["source"]['name']
    title1=read["articles"][0]["title"]
    description1=read["articles"][0]["description"]
    url1=read["articles"][0]["url"]
    
    source2=read["articles"][1]["source"]['name']
    title2=read["articles"][1]["title"]
    description2=read["articles"][1]["description"]
    url2=read["articles"][1]["url"]
    
    source3=read["articles"][2]["source"]['name']
    title3=read["articles"][2]["title"]
    description3=read["articles"][2]["description"]
    url3=read["articles"][2]["url"]
    
    return source1, title1, description1, url1, source2, title2, description2, url2, source3, title3, description3, url3
    
    

@client.event
async def on_message(message):
    contents=message.content.split(" ")
    if message.author == client.user:
        return
               
   
#------Looking for commands---------------------------------------------------"""  
    
    if message.content.startswith('?'):   
        if message.content in commandList or message.content in newsCategories or '?google' in message.content or '?say' in message.content:
            pass
        else:
            await client.send_message(message.channel, "__`Sorry, I didn't catch that. For things I can help you with, type '?help'.`__")

#-------------------------------------------------------------------------------"""
#--------Google ----------------------------------------------------------------"""        
    #This is the module used for the code below:
    #https://pypi.org/project/beautifulsoup4/ 
    #And also, this code is not written by me 
      
    if message.content.lower().startswith("?google"):
        url = message.content.lower()
        url = url[8:]

        reply=":small_blue_diamond:Here are the top three results for your search {0.author.mention}:".format(message)
        await client.send_message(message.channel, reply)
        
        for search1 in search(url, tld="com", num=3, stop=1, pause=2):
            await client.send_message(message.channel, "<" + search1 + ">")
    
#-----------------------------------------------------------------------------"""
#-----Date&Time---------------------------------------------------------------"""
    #To understand how to work with time in python I used this: 
    #https://www.techatbloomberg.com/blog/work-dates-time-python/
    
    if message.content=='?time':
        url= "http://worldtimeapi.org/api/timezone/Europe/London.txt"
        datetime=dt.datetime.now().isoformat()
        reply=datetime[11:16]
        await client.send_message(message.channel, ':small_blue_diamond: `Here is the time: ' + reply + '`')
        
        
    if message.content=='?date':
        datetime=dt.datetime.now().isoformat()
        day=datetime[8:10]
        month=datetime[5:7]
        year=datetime[0:4]
        await client.send_message(message.channel, ':small_blue_diamond: `Day: ' + day + '`' )
        await client.send_message(message.channel, ':small_blue_diamond: `Month: '+ month + '`')
        await client.send_message(message.channel, ':small_blue_diamond: `Year: '+ year + '`')
        
#-----End of Date&Time-------------------------------------------------------"""        
    
    if message.content=="?help":
        reply1="Hello {0.author.mention}".format(message)
        reply2="This are the commands that you can use at the moment(most of them are self explanatory):"
        reply3=":small_blue_diamond: Use '?google' for a quick google search."
        reply4=":small_blue_diamond: Use '?rating' to get a chance to rate me. "
        reply5=":small_blue_diamond: Use '?news' to find out the top three articles today about the topic of your choice. "
        reply6=":small_blue_diamond: Use '?date' to find out the date."
        reply7=":small_blue_diamond: Use '?time' to find out the time. "
        reply8=":small_blue_diamond: Use '?say' to make me say something. "
        
        await client.send_message(message.channel, reply1 + '\n' + reply2 + '\n' +  reply3 + '\n' + reply4 + '\n' +  reply5 + '\n' + reply6 + '\n' + reply7 + '\n' +  reply8)
       
    
#---------News api-------------------------------------------------------""" 
    #https://newsapi.org/docs/get-started
    #This is the website that I used to get the API 
    #I also used it to understand how do the parameters work
    #(For example, the country, the keyword, which is noted by 'q', and also the category)
    #This information can be found here: https://newsapi.org/docs/endpoints/top-headlines
   

    if message.content=='?news':
        reply1="Please choose a category: business, sports, entertainment, general, science, health, technology."
        reply2="Don't forget to use '?' before."
        reply3="If you're searching for a specific topic, then just type '!' and then your keyword. "
        await client.send_message(message.channel, '`' + reply1 + '\n' + reply2 + '`' + ':blush:' + '\n' + '`' + reply3 + '`')
        
    if message.content in newsCategories:
        presentation="Here are the top three news articles in the category that you selected, {0.author.mention}.".format(message)
        cat=str(message.content)
        category=cat[1:]
        list_news=list(await news_search(await news_category(category)))
        
        try:
        
            source1=list_news[0]
            title1=list_news[1]
            description1=list_news[2]
            link1=list_news[3]

            source2=list_news[4]
            title2=list_news[5]
            description2=list_news[6]
            link2=list_news[7]

            source3=list_news[8]
            title3=list_news[9]
            description3=list_news[10]
            link3=list_news[11]




            await client.send_message(message.channel, presentation + '\n' + ':small_blue_diamond: Number 1:' + '\n' + 'Source: ' + source1 + '\n' + 'Title: ' + title1 + '\n' + 'Description: ' + description1 + '\n' + '<' + link1 + '>' + '\n' + ':small_blue_diamond: Number 2: ' + '\n' + 'Source: ' + source2 + '\n' + 'Title: ' + title2 + '\n' + 'Description: ' + description2 + '\n' + '<' + link2 + '>' + '\n' + ':small_blue_diamond: Number3: ' + '\n' + 'Source: ' + source3 + '\n' + 'Title: ' + title3 + '\n' + 'Description: ' + description3 + '\n' + '<' + link3 + '>')
            
            
        except:
            await client.send_message(message.channel, 'Sorry there are not enough articles in that category. You can try another one if you want, {0.author.mention}.'.format(message))
        
        
       
    
    if message.content.startswith('!'):
        presentation="Here are the first three articles containing the keyword that you entered,  {0.author.mention}.".format(message)
        mes=str(message.content)
        keyword=mes[1:]
        list_news=list(await news_search(await news_keyword(keyword)))
       
        
        if len(list_news)==12:
            source1=list_news[0]
            title1=list_news[1]
            description1=list_news[2]
            link1=list_news[3]

            source2=list_news[4]
            title2=list_news[5]
            description2=list_news[6]
            link2=list_news[7]

            source3=list_news[8]
            title3=list_news[9]
            description3=list_news[10]
            link3=list_news[11]
           
            await client.send_message(message.channel, presentation + "\n" + ":small_blue_diamond: Number 1:" + "\n" + "Source: " + source1 + "\n" + "Title: " + title1 + "\n" + "Description: " + description1 + "\n" + "<" + link1 + ">" + "\n" + ":small_blue_diamond: Number 2:" + "\n" + "Source: " + source2 + "\n" + "Title: " + title2 + "\n" + "Description: " + description2 + "\n" + "<" + link2 + ">" + "\n" + ":small_blue_diamond: Number 3:" + "\n" + "Source: " + source3 + "\n" + "Title: " + title3 + "\n" + "Description: " + description3 + "\n" + "<" + link3 + ">")
     
        
        
        else:
            await client.send_message(message.channel, await news_search(await news_keyword(keyword)))

#----------------------------------------------------------------------------------"""        
        
    
    
    if message.content.upper().startswith("WHAT'S YOUR NAME?") or message.content.upper().startswith("WHATS YOUR NAME") or message.content.upper().startswith("WHAT'S YOUR NAME"):
        reply="My name is Dave. It is a pleasure to meet you {0.author.mention}. :grinning:".format(message)
        await client.send_message(message.channel,reply)
        
    if message.content.upper().startswith('?SAY'):
        m1=message.content.split(" ")
        await client.send_message(message.channel,'`'+(" ".join(m1[1:]))+'`')
        
    if message.content.upper().startswith('AWE') or message.content.upper().startswith('AW') or message.content.upper().startswith("AWW"):              
        reply=["awe",
        ":heart_eyes:"]
        await client.send_message(message.channel,random.choice(reply))
    
    
    if message.content.upper().startswith('HI') or message.content.upper().startswith('HELLO') or message.content.upper().startswith('HEY') or message.content.upper().startswith('HEYY') :
        reply ="Hello there {0.author.mention} and welcome to my server. Don't forget to use the prefix '?' for commands.".format(message)
        await client.send_message(message.channel, reply)
                  
    if message.content.upper().startswith("HOW ARE YOU?") or message.content.upper().startswith("HOW ARE YOU") or message.content.upper().startswith("HOW ARE U") or message.content.upper().startswith("HOW'S IT GOING?") or message.content.upper().startswith("HOW'S IT GOING"):
        reply=["Much better now that you are with me.",
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
        
    if message.content.upper().startswith("YOU'RE BEAUTIFUL") or message.content.upper().startswith("YOU ARE BEAUTIFUL") or message.content.upper().startswith("YOU'RE SO HANDSOME") or message.content.upper().startswith("YOU ARE PRETTY") or message.content.upper().startswith("YOU'RE PRETTY"): 
        reply=["You must be looking at a mirror.",
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
        await client.send_message(message.channel,random.choice(reply))
        await client.send_file(message.channel, 'robot.photo.jpg')
        

    for word in contents:
        if word in thanks_list:
            reply=["I'm happy to help.",
              "You got it.",
              "My pleasure.",
              "Anytime.",
              "No worries.",
              "Don't mention it."]
            await client.send_message(message.channel, '`' + random.choice(reply) + '`')
  

    if message.content.upper().startswith("WHAT IS THE MEANING OF LIFE") or message.content.upper().startswith("WHAT'S THE MEANING OF LIFE?") or message.content.upper().startswith("WHAT'S THE MEANING OF LIFE") or message.content.upper().startswith("WHAT IS THE MEANING OF LIFE?"):
        reply=["To die.",
          "I don't think there is one. I think it's all just a series of incredible, beautiful, and meaningless coincidences, which we might as well enjoy.",
          "I give up.",
          "42",]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')
        
    if message.content.upper().startswith("HAHA") or message.content.upper().startswith("HAH") or message.content.upper().startswith("HAHAH") or message.content=="ha":
        reply=["I'm happy I made you laugh",
          ":joy: :joy: :joy:",
          ":wink:",
          ":sweat_drops: :sweat_drops: :peach:"]
        await client.send_message(message.channel,random.choice(reply)) 
    
    
    if message.content.upper().startswith("DAVE?") or message.content.upper().startswith("DAVE") or message.content.upper().startswith("DAV") or message.content.upper().startswith("DAV?"):
        reply=["Yes?",
          "Right here."
          "How may I help you?",
          "Oh, you again.",
          "Still here."]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')
        
        
    if message.content.upper().startswith("BYE") or message.content.upper().startswith("GOODBYE") or message.content.upper().startswith("GOODNIGHT"):
        reply=["Bye bye",
          "See you next time!",
          "Take care.",
          "Hav a nice day!",
          "I'll be right here waiting for you."]
        await client.send_message(message.channel, '`' + random.choice(reply) + '`')
       
    
    if message.content.upper().startswith('?RATING'):
        msg = await client.send_message(message.channel, '`Let me know what you think about me. React with thumbs up or thumbs down.`')
        res = await client.wait_for_reaction(['👍', '👎'], message=msg)
        await client.send_message(message.channel, '`{0.user} thank you for your reaction {0.reaction.emoji}!`'.format(res))

   
    if message.content.endswith('?'):
        reply=["Signs point to yes.",
          "Without a doubt.",
          "As I see it, yes.",
          "Better not tell you now.",
          "Most likely.",
          "My reply is no.",
          "Don't count on it.",
          "No."]
        await client.send_message(message.channel,'`' + random.choice(reply) + '`')
        
    if message.content.upper().startswith("LET'S") or message.content.upper().startswith("LETS"):
        reply=["Hell no", 
          "Hell yes",
          "I'm down"]
        await client.send_message(message.channel, random.choice(reply))
        
        
        
        
        
client.run(TOKEN)
