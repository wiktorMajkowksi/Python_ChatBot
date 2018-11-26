cAke = ["Carrot cake", "Chocolate cake", "Caramel cake"]
end = ("thanks", "ty")

from Validation import validation
check = ("")

def flavors2(cAke):
	"""This function selects the output and assignes it to a letter"""
	print("a) Carrot cake")
	print("b) Chocolate cake")
	print("c) Caramel cake")
	userInput = input("You: ").lower()
	if userInput == "a":
		return cAke.pop(0)
	elif userInput == "b":
		return cAke.pop(1)
	elif userInput == "c":
		return cAke.pop(2)
	elif userInput in end:
		exit()
		"""This ends the conversation with CHAT_BOT"""
	else:
		validation(check)
		print("CHAT_BOT: Sorry, I don't know this flavor.")
		print("CHAT_BOT: What Flavor would you like?")
		flavors2(cAke)

print("CHAT_BOT: I will bring you " + str(flavors2(cAke)))
"""It prints the output of the function"""