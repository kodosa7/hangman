# terminal game of hangman
# (c) 03/2020

from random import randint
from data import hangman, words, title_ascii, win_ascii, game_over_ascii


# print title ascii label
for line in range(len(title_ascii)):
    print(title_ascii[line][0])

# set variables
random_word = words[randint(0, len(words) - 1)]
level = 1
old_answer = "-"
bad_tried_letters = ""
letters_tried_twice = []
guessed = []

print("\nThe hidden word has",len(random_word),"characters.")

while level < 13:
    ''' main loop '''

    for pismeno in range(len(random_word)):
        ''' letter counter loop'''

        random_word_list = list(random_word)

        # user input
        answer = input(f"\n.: Round {level} :: Guess a letter (a-z): ")

        # check for allowed chars
        if answer < "a" or answer > "z" or len(answer) > 1:
            print("\nWrong input! Enter single small letters only.")
            break

        # check for repeated answer
        if answer not in letters_tried_twice:
            letters_tried_twice.append(answer)
        else:
            print("\nYou've guessed this letter in the previous turn already!\n")
            break

        # letter is in the word
        if answer not in random_word:
            print()
            for line in range(len(hangman[level])):
                print(hangman[level][line][0])

            print("\nI'm, sorry, but the word doesn't contain letter", answer.upper(), "! :-(\n")
            bad_tried_letters += answer + ","
            print("Wrong letters already tried:", bad_tried_letters.upper(), "\n")
            level += 1

        # letter is not in the word
        elif answer in random_word:
            print("\nHooray! Letter", answer.upper(), "is there! :-)\n")
            old_answer = answer
            for same_letter_count in range(random_word_list.count(answer)):
                guessed.append(answer)

        # print word pattern
        print("[", end="")
        for letter in random_word:
            if letter in guessed:
                print(letter.upper(), end="")
            else:
                print("-", end="")
        print("]\n")

        # win
        if len(guessed) == len(random_word):
            for line in range(len(win_ascii)):
                print(win_ascii[line][0])

            level = 13
        break

# game over
for line in range(len(win_ascii)):
    print(game_over_ascii[line][0])
print()
