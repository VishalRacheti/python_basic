random_words=["python", "hangman", "challenge", "programming", "development", "function", "variable", "iteration", "condition", "syntax"]

import random


#Todo-1: Randomly choose a word from the random_words list and assign it to the variable choosen_word

choosen_word = random.choice(random_words)
print(choosen_word)  # For testing


#Placeholder for user to guess letter

placeholder = "_ " * len(choosen_word)
print(placeholder)

#Todo-2: Ask the user to guess a letter and assign their anwer to a variable called guess_letter.make guess_letter lowercase.

guess_letter = input("Guess a letter: ").lower()



#Todo-3: Check if the letter the user guessed (guess_letter) is one of the letters in the choosen_word.print right if it is , wrong if it is not.

for letter in choosen_word:
    print(letter)
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")