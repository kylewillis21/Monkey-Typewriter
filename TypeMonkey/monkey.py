# this is the monkey typewriter hypothesis
import string
import random
import time
import re
import threading


# First thing that needs to be done is to create a way to randomly generate a letter of the alphabet
def randoLetter():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    return random.choice(characters)

# Create a list out of the words in the hamlet file
def hamList():
    file = open('hamlet.txt')
    hamlet = []
    for word in file.read().split():
        word = re.sub(r'[^a-zA-Z0-9]', '', word)
        hamlet.append(word)
    return hamlet

hamlet = hamList()

# Make the list all lowercase
def lowerCase(list):
    for i in range(len(list)):
        list[i] = list[i].lower()
    return list
hamlet = lowerCase(hamlet)

# Remove the duplicate words in the list to make the process easier
def rmvDups(list):
    output = []
    [output.append(x) for x in list if x not in output]
    return output


hamlet = rmvDups(hamlet)
# These are due to the fact that I want this process to end at some point
hamlet.remove("tragicalcomicalhistoricalpastoral")
hamlet.remove("historicalpastoral")
hamlet.remove("tragicalhistorical")
hamlet.remove("somethingsettled")
hamlet.remove("liberalconceited")
hamlet.remove("seemingvirtuous")
hamlet.remove("pastoralcomical")
hamlet.remove("sentinelsfirst")
hamlet.remove("shrillsounding")
hamlet.remove("fortifications")
# hamlet.remove("")
# hamlet.remove("")
# hamlet.remove("")
# hamlet.remove("")
# hamlet.remove("")
# hamlet.remove("")

# Make a list for each monkey to use separately
ham2 = ham3 = hamlet

# Create the list that compares the random string and the strings of hamlet
def monkey(name):
    totStr = ''
    totWrds = 0
    total = len(hamlet)
    print("THERE ARE " + str(total) + " WORDS IN HAMLET")
    while True:
        randomLetter = randoLetter()
        totStr = totStr + randomLetter
        # print(randomLetter)
        # time.sleep(1)
        if len(totStr) >= 30:
            totStr = ''
        for x in hamlet:
            if x in totStr:
                hamlet.remove(x)
                # print(foundWrds)
                totWrds += 1
                print(name + ' FOUND ' + x + " IN HAMLET")
                print(name + " HAS FOUND " + str(totWrds) + " WORDS")
                # time.sleep(1)
        if totWrds == total:
            print("All words have been found in Hamlet!")
            break

def monkey2(name):
    totStr2 = ''
    totWrds2 = 0
    total2 = len(ham2)
    print("THERE ARE " + str(total2) + " WORDS IN HAMLET")
    while True:
        randomLetter = randoLetter()
        totStr2 = totStr2 + randomLetter
        # print(randomLetter)
        # time.sleep(1)
        if len(totStr2) >= 30:
            totStr2 = ''
        for x in ham2:
            if x in totStr2:
                ham2.remove(x)
                # print(foundWrds)
                totWrds2 += 1
                print(name + ' FOUND ' + x + " IN HAMLET")
                print(name + " HAS FOUND " + str(totWrds2) + " WORDS")
                # time.sleep(1)
        if totWrds2 == total2:
            print("All words have been found in Hamlet!")
            break  

def monkey3(name):
    totStr3 = ''
    totWrds3 = 0
    total = len(ham3)
    print("THERE ARE " + str(total) + " WORDS IN HAMLET")
    while True:
        randomLetter = randoLetter()
        totStr3 = totStr3 + randomLetter
        # print(randomLetter)
        # time.sleep(1)
        if len(totStr3) >= 30:
            totStr3 = ''
        for x in ham3:
            if x in totStr3:
                ham3.remove(x)
                # print(foundWrds)
                totWrds3 += 1
                print(name + ' FOUND ' + x + " IN HAMLET")
                print(name + " HAS FOUND " + str(totWrds3) + " WORDS")
                # time.sleep(1)
        if totWrds3 == total:
            print("All words have been found in Hamlet!")
            break 

# GET THEM MONKEYS GOING           
Cletus = threading.Thread(
    target=monkey, args=("Cletus",)
)
Lionel = threading.Thread(
    target=monkey2, args=("Lionel",)
)
Mabel = threading.Thread(
    target=monkey3, args=("Mabel",)
)

# Start the monkeys
Cletus.start()
Lionel.start()
Mabel.start()

# Join the monkeys
Cletus.join()
Lionel.join()
Mabel.join()

# monkey("Mabel")

# def longestWrd():
#     long = 0
#     word = ''
#     for i in range(len(hamlet)):
#         if len(hamlet[i]) > long:
#             long = len(hamlet[i])
#             word = hamlet[i]

#     print("THE LONGEST WORD IS " + word + " AND IS " + str(long) + " LETTERS LONG")  

# longestWrd()