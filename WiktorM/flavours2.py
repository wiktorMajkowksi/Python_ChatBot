fruit = ["Strawberries", "Blackcurrants", "Blueberries", "Oranges"]
end = ("thanks", "ty")
from Validation import validation
check = ("")

def flavors3(fruit):
	"""This function selects the output and assignes it to a letter"""
	print("a) Strawberries")
	print("b) Blackcurrants")
	print("c) Blueberries")
	print("d) Oranges")
	userInput = input("You: ").lower()
	if userInput == "a":
		return fruit.pop(0)
	elif userInput == "b":
		return fruit.pop(1)
	elif userInput == "c":
		return fruit.pop(2)
	elif userInput == "d":
		return fruit.pop(3)
	elif userInput in end:
		exit()
		"""This ends the conversation with CHAT_BOT"""
	else:
		validation(check)
		print("CHAT_BOT: Sorry, I don't know this flavor.")
		print("CHAT_BOT: What Flavor would you like?")
		flavors3(fruit)	
		
print("CHAT_BOT: I will bring you a bowl of " + str(flavors3(fruit)))
"""It prints the output of the function"""