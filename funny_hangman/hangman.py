 ###########
#           #
#    +---+  #
#    |   |  #
#    O   |  #
#   /|\  |  #
#   / \  |  #
#        |  #
#  =======  #
 ###########


import os
import random

def build_hangman(hangman, position):
    if position == 1:
        hangman = list(hangman)
        hangman[46], hangman[38], hangman[30], hangman[22], hangman[14] = "|", "|",  "|", "|", "|"
        hangman = "".join(hangman)
        return hangman

    if position == 2:
        hangman = list(hangman)
        hangman[2], hangman[3], hangman[4], hangman[5], hangman[6] = "+", "-", "-", "-", "+"
        hangman = "".join(hangman)
        return hangman
    
    if position == 3:
        hangman = list(hangman)
        hangman[10] = "|"
        hangman = "".join(hangman)
        return hangman
    
    if position == 4:
        hangman = list(hangman)
        hangman[18] = "0"
        hangman = "".join(hangman)
        return hangman

    if position == 5:
        hangman = list(hangman)
        hangman[26] = "|"
        hangman  = "".join(hangman)
        return hangman

    if position == 6:
        hangman = list(hangman)
        hangman[25], hangman[27] = "/", "\\"
        hangman  = "".join(hangman)
        return hangman
    
    if position == 7:
        hangman = list(hangman)
        hangman[33] = "/"
        hangman = "".join(hangman)
        return hangman

    if position == 8:
        hangman = list(hangman)
        hangman[35] = "\\"
        hangman = "".join(hangman)
        return hangman

#46 38 30 22
#2 => +; 3 => -; 4 => -; 5 => +;
#10 => |
#18 => 0
#25 => /; 26 => |; 27 => \;
#33 => /; 35 => \;

def get_words():
    wordlist = []
    file = open('wordlist.txt')
    for i in file.readlines():
        wordlist.append(i.replace('\n', '').lower())
    return wordlist

def init_game():
    hidden = ""
    wordlist = get_words()
    word = wordlist[random.randint(0, 100)]
    
    for i in range(len(word)):
        hidden = hidden + "_"
    return hidden, word
    
def play():
    hidden, word = init_game()
    wrong_letters = []
    hangman = "       \n       \n       \n       \n       \n       \n======="
    win = False

    while True:
        found = False
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" , wrong_letters)
        print(hangman)
        print(hidden)
        char = input("Enter a letter: ")
        if char == "":
            print("Enter a valid letter")
            continue
        if char == word:
            win = True
            break

        for i in range(len(word)):
            if char[0] == word[i]:
                found = True
                hidden = list(hidden)
                hidden[i] = char[0]
                hidden = "".join(hidden)

        if found == False:
            wrong_letters.append(char[0])
            if len(wrong_letters) == 9:
                break

            hangman = build_hangman(hangman, len(wrong_letters))

    if win == True:
        print("You win! :)")
    else:
        print("You lost! :(")
        print("The word was: " + word + "\n")
print("---------------Hangman---------------\n ########### \n#           #\n#    +---+  #\n#    |   |  #\n#    O   |  #\n#   /|\  |  #\n#   / \  |  #\n#        |  #\n#  =======  #\n ###########")

start = input("Do you now how to play? (y|n) ")
if start == "n":
    print("An unknown word is drawn at random. Which you have to guess  \nby trying letter by letter. If you know the word, type it in the \nsame field where you typed the letters. \nThen you win!")
else:
    print("Let's begin!")
input()

while True:
    play()
    start = input("Do you want to play again? (y|n) ")
    if start != "y":
        break