#Ian Turner | Sept 18 2023 | WordScramble

import os
import random

def printASCII(guesses):
    os.system('clear')
    if(guesses == 3):
        print("  ████  ████       ████  ████      ████  ████ ")
        print(" ████████████     ████████████    ████████████ ")
        print("  ██████████       ██████████      ██████████ ")
        print("   ████████         ████████        ████████ ")
        print("      ██               ██              ██ ")
    elif(guesses == 2):
        print("  ████  ████       ████  ████      □□□□  □□□□ ")
        print(" ████████████     ████████████    □□□□□□□□□□□□ ")
        print("  ██████████       ██████████      □□□□□□□□□□ ")
        print("   ████████         ████████        □□□□□□□□ ")
        print("      ██               ██              □□ ")
    else:
        print("  ████  ████       □□□□  □□□□      □□□□  □□□□ ")
        print(" ████████████     □□□□□□□□□□□□    □□□□□□□□□□□□")
        print("  ██████████       □□□□□□□□□□      □□□□□□□□□□")
        print("   ████████         □□□□□□□□        □□□□□□□□")
        print("      ██               □□              □□")

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

while True:
    word_list = ["apple", "banana", "cherry", "grape", "orange",
             "strawberry", "blueberry", "watermelon", "pineapple", "kiwi",
             "peach", "mango", "lemon", "lime", "coconut",
             "apricot", "pomegranate", "blackberry", "raspberry", "pear"]

    word1 = random.choice(word_list)
    word2 = random.choice(word_list)
    word3 = random.choice(word_list)
    randWord = scramble_word(word1 + word2 + word3)
    attempts = 3

    while True:
        print("Scrambled word:", randWord)
        print("Guess one of the words:", word_list)
        guess = input("Your guess: ")

        if guess == word1 or guess == word2 or guess == word3:
            for letter in guess:
                randWord = randWord.replace(letter, ' ', 1)
            printASCII(attempts)
            print("Correct!")
            if randWord.strip() == '':
                print("Victory!")
                break
        else:
            attempts -= 1
            printASCII(attempts)
            print("Incorrect!")
            if attempts == 0:
                print("Failure!")
                break

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break
