#deserts
desertInput = ("ice-cream", "cake", "fruits", "nothing")
desertOutput = ("What flavour would you like?")
end = ("thanks", "ty", "bye", "see you later", "exit", "q")
endOutput = ("Bye (-_-)", "See you later ^,^", "Till the next time :)")
import random
"""This imports the random function from python standard library"""

a = ("")
from Validation import validation
check = ("")


print("\/"*30)
print("CHAT_BOT: What would you like to eat for yout dersert?")
print()
print("CHAT_BOT: I can offer you the following:")
print("          ice-cream: £2 (add an extra scoop for 50p).")
print("          cake: £3 per slice.")
print("          fruits: £1 per bowl.")
"""Those print commands create a welcome interface"""

def ask_which_desert(sentence):
	"""This function outputs question based on input"""
	for word in sentence.split(' '):
		"""This splits the user's input"""
		if word in desertInput:
			return desertOutput
		elif word in end:
			print("CHAT_BOT: " + str(random.choice(endOutput)))
			"""This chooses a random string from endOutput"""
			exit()
		else:
			return "Could you repeat?"
			
		
while True:
	"""This loops the CHAT_BOT"""
	sentence = input("You: ").lower()
	"""This enforces lower case letters"""
	responce = ask_which_desert(sentence)
	if sentence == "ice-cream":
		print("CHAT_BOT: " + str(responce))
		from flavors import flavors1
		from somethingElse import something
		something(a)
		
	elif sentence == "cake":
		print("CHAT_BOT: " + str(responce))
		from flavours1 import flavors2
		from somethingElse import something
		something(a)
		

	elif sentence == "fruits":
		print("CHAT_BOT: " + str(responce))
		from flavours2 import flavors3	
		from somethingElse import something
		something(a)
	
	
	else:
		validation(check)
		print("What desert do you want?")
		ask_which_desert(sentence)
		
		