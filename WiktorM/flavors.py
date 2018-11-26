iceCream = ["Chocolate", "Strawberry", "Lemon", "Toffi", "Vanilla"]
end = ("thanks", "ty")

from Validation import validation
check = ("")

def flavors1(iceCream):
	"""This function selects the output and assignes it to a letter"""
	print("a) Chocolate")
	print("b) Strawberry")
	print("c) Lemon")
	print("d) Toffi")
	print("e) Vanilla")
	userInput = input("You: ").lower()
	if userInput == "a":
		return iceCream.pop(0)
	elif userInput == "b":
		return iceCream.pop(1)
	elif userInput == "c":
		return iceCream.pop(2)
	elif userInput == "d":
		return iceCream.pop(3)
	elif userInput == "e":
		return iceCream.pop(4)
	elif userInput in end:
		exit()
		"""This ends the conversation with CHAT_BOT"""
	else:
		validation(check)
		print("CHAT_BOT: Sorry, I don't know this flavor.")
		print("CHAT_BOT: What Flavor would you like?")
		flavors1(iceCream)
			


#if ask_which_desert == "ice-cream":	
#	print(flavors1(iceCream))
#elif ask_which_desert == "cake":
#	print(flavors2(cAke))
#elif ask_which_desert == "fruits":
#	print(flavors3(fruit))
#else:
#	print("ERROR")
print("CHAT_BOT: I will bring you " + str(flavors1(iceCream)) + " ice-cream.")
"""It prints the output of the function"""