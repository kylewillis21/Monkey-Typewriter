# this is the monkey typewriter hypothesis
import string
import random
import time
import re
import threading
import queue


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

# Make a list for each monkey to use separately
ham2 = ham3 = hamlet

# Must create a lock for when the monkeys access and modify the list
lock = threading.Lock()

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
        if len(totStr) >= 30: # This is needed so that way the word can reset if it gets too long
            totStr = ''
        with lock:
            for x in hamlet[:]: # We iterate over a shallow copy to avoid modification during iteration
                if x in totStr:
                    hamlet.remove(x)
                    totWrds += 1
                    print(name + ' FOUND \"' + x + "\" IN HAMLET")
                    print(name + " HAS FOUND " + str(totWrds) + " WORDS\n")
            if totWrds == total:
                print("All words have been found in Hamlet!")
                break

Cletus = threading.Thread(
    target=monkey, args=("Cletus",)
)

Lionel = threading.Thread(
    target=monkey, args=("Lionel",)
)

Mabel = threading.Thread(
    target=monkey, args=("Mabel",)
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