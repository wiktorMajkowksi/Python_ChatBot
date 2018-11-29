import json
import urllib.request

'###ChatBot using API to retrieve information about countries###'

def validate(user_input):
    allowedInputs = ["name", "flag", "native name", "currency name", "native language", "region"]
    while user_input == False:
        user_input = input("Enter a topic of information: ")
        user_input = user_input.lower()
        if user_input not in allowedInputs:
            user_input = False
    return user_input

def choice_2():
    main_url = 'http://countryapi.gear.host/v1/Country/getCountries?'
    response = urllib.request.urlopen(main_url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)
    user_input = False
    print("Here is a list of Information Please Select One: \n- Name \n- Flag \n- Native Name")
    print("- Currency Name \n- Native Language \n- Region")
    user_input = validate(user_input)
    user_input = user_input.title()
    user_input2 = user_input.replace(" ", "")  # string method

    if user_input == "Region":
        '###code modified from '
        list1 = list()
        print("Here's a list of all the Continents")
        for item in data['Response']:
            list1.append(item[user_input])
        continents = set(list1)
        print(continents)
    else:
        print("Here's a list of all the Countries Information about their", user_input, ": ")
        for item in data['Response']:
            print(item[user_input2])

    next_choice(next)

def choice_1():
    country_url = 'http://countryapi.gear.host/v1/Country/getCountries?pName='

    search_country = input('Please Enter A Country You Would Like To Search:')
    search_country2 = search_country.lower()
    search_country2 = search_country2.replace(" ", "%")

    search_response = country_url + search_country2
    response = urllib.request.urlopen(search_response).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)

    user_input = False
    print("Here is a list of Information Please Select One: \n- Flag \n- Native Name \n- Currency Name\n- Native Language")
    user_input = validate(user_input)
    user_input2 = user_input.title()
    user_input2 = user_input2.replace(" ", "")  # string method

    print("Here's the ", user_input, "for", search_country)
    for item in data['Response']:
        print(item[user_input2])

    next_choice(next)

def next_choice(next):
    print("What else would you like to know? ")
    print("Here are some choices: \n1. Find Information about a certain country, \n2. Find information about all countries\n3. Exit")
    next = input("Enter here:")

    if next == "1":
        choice_1()
    elif next == "2":
        choice_2()
    elif next == "3":
        print("Ok, See you Next Time!!")
        quit()
    else:
        next = ("That wasn't an option try again: ")
        next_choice(next)

def choice_made(choice):
    if choice == "1":
        choice_1()
    elif choice == "2":
        choice_2()
    else:
        '###validation of users input uses recursion###'
        print("Sorry, but your input wasn't an option")
        choice = input("Please Try Again: ")
        choice_made(choice)


def Main_Program():
    print('Hey! Welcome Back \nWhat would you like to know today?')
    print("Here are some choices: \n1. Find Information about a certain country, \n2. Find information about all countries ")
    choice = input("Let us know here (please enter the number): ")
    choice_made(choice)


Main_Program()
