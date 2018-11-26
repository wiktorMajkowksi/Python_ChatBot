sentence = ("")

yesInput = ["yes", "sure", "of course"]
noInput = ["no", "thanks", "bill please"]

from Validation import validation
check = ("")

def something(a):
	print()
	print("CHAT_BOT: Can I get you anything else?")
	userInput = input("You: ").lower()
	"""This enforces lower case letters"""
	if userInput in yesInput:
		from chatBot_v1 import ask_which_desert
		ask_which_desert(sentence)
	elif userInput in noInput:
		print("CHAT_BOT: I will generate the bill")
		exit()
	elif userInput in end:
		exit()
	else:
		validation(check)
		something(a)
		"""This calls the same function again"""
		#I have done this to force user to choose one of the options provided
	
	