scoops = ("How many scoops would you like?")

def numScoops(scoops):
	userInput = input("You: ").lower()
	return userInput

print(scoops)
userInput = ("")
print("I will bring " + numScoops(scoops) + " scoops.")