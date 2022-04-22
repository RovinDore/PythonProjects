#lw - lowest winning number previous
#hist - history of number played from all previous round
#lc - choice for previous round
#n - number of players
#y - position in lc list

import random
# import matplotlib.pyplot as plt

def randomChoice():
    return random.randint(0, 100)

#function to get unique choices nad amount of times a number appears
def checkUnique(playerChoices):
    unique = [] #store unique values
    options = {} #
    numberAppearance = {} #this is to store how many times a number shows up
    #loop through choices
    for choice in playerChoices:
        #if choice not in uniqe list 
        if choice not in unique: 
            unique.append(choice) #add to unique list
            numberAppearance[choice] = 1 #add to number appearance
        else:
            #since in unique list check to see if already in appearance list
            if choice in numberAppearance: 
                numberAppearance[choice] = numberAppearance[choice] + 1 # add 1 to value if already exist
            else:
                numberAppearance[choice] = 1 # start at one
    
    unique.sort() #sort unique list so lowest is the first value
    #add values to options dictionary
    options["lowestUnique"] = unique[0]
    options["numberAppearance"] = numberAppearance
    return options

#1 round of game
def playGame(amountOfPlayers):
    gameDetails = {
        "winningNumber": "",
        "playerChoices": [],
    }
    thisRoundChoices = []

    #loop for amount of player
    i = 0
    while(i < amountOfPlayers):
        thisRoundChoices.append(randomChoice()) #each player choose a random number
        i += 1
    
    z = checkUnique(thisRoundChoices) #save the choices values (lowest unique number and how many times a number appears)
    gameDetails["playerChoices"] = thisRoundChoices
    gameDetails["winningNumber"] = z["lowestUnique"]
    gameDetails["numberAppearance"] = z["numberAppearance"]
    return gameDetails


print("Begining the game")
currentRound = 0
maxRounds = 10
numberOfPlayers = 50
historyNumber = []
lw = 100
lc = []
while(currentRound < maxRounds):
    thisRound = playGame(numberOfPlayers)
    lc = thisRound["playerChoices"]
    historyNumber.append(thisRound["numberAppearance"])
    lw = thisRound["winningNumber"]
    currentRound += 1
    print("round ", currentRound)
    print("winning number ", lw)
    print("last choices ", lc)
    print()

print(historyNumber)
# plt.hist(historyNumber, bins=numberOfPlayers)
# plt.title("Histogram")
# plt.ylabel("Frequency")
# plt.xlabel("Player Choices")
# plt.show()
