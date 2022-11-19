import os
import random
from hangman_stuff import *


game_state = None
difficulty = ""


def game_setup():
    global difficulty
    lives = ()
    type_of_game = ""
    while type_of_game == "":
        type_of_game = input("Do you want to enter a custom word or use a random word? [C/R] ")
        if type_of_game == "C":
            word_to_guess = input("What is the word? ")
            word_to_guess = word_to_guess.lower()
        elif type_of_game == "R":
            word_to_guess = wordbank[random.randint(0, len(wordbank) + 1)]
        else:
            type_of_game = ""
    while type(lives) != int:
        os.system("cls")
        print("What difficulty do you want to play?\nNormal: 6 lives\nHard: 3 lives\nInsane: 1 life")
        difficulty = input("Enter here: ")
        if difficulty == "Normal":
            lives = 6
        elif difficulty == "Hard":
            lives = 3
        elif difficulty == "Insane":
            lives = 1
    settings = [lives, word_to_guess]
    os.system('cls')
    return settings


def encode_word(word):
    encoded_word = ""
    for i in word:
        if i == " ":
            encoded_word += i
        else:
            encoded_word += "_"
    return encoded_word


def hangmandrawing(difficulty, lives):
    if difficulty == "Normal":
        return (HANGMANPICS[-(lives + 1)])
    if difficulty == "Hard":
        return(HANGMANPICS[-(lives * 2 + 1)])
    if difficulty == "Insane":
        return(HANGMANPICS[-(lives * 6 + 1)])


def hangman(word, guessed_letters, lives, key, missed_letters):
    global game_state
    new_parameters = [word, guessed_letters, lives, key, missed_letters]
    while game_state == None:
        word = new_parameters[0]
        guessed_letters = new_parameters[1]
        lives = new_parameters[2]
        key = new_parameters[3]
        new_parameters = hangmanguess(word, guessed_letters, lives, key, missed_letters)


def hangmanguess(word, guessed_letters, lives, key, missed_letters):
    global difficulty
    encoded_word = ""
    lives = lives
    if (word != encoded_word) and lives != 0:
        guess = input("Guess a letter or the whole word: ").lower()
        if len(guess) == 1:
            if guess in word:
                guessed_letters += [guess]
                encoded_word = ""
                for i in word:
                    if i == " " or i in guessed_letters:
                        encoded_word += i
                    else:
                        encoded_word += "_"
                key = encoded_word
            else:
                if guess not in missed_letters:
                    missed_letters += [guess]
                lives -= 1
                encoded_word = key
        elif len(guess) > 1:
            if guess == word:
                encoded_word = word
                key = word
            elif guess != word:
                lives = 0
                missed_letters += [guess]
        os.system('cls')
        print(hangmandrawing(difficulty, lives))
        print("Word:", key, "\nMissed Letters:", missed_letters, "\nLives:", lives)
        win_or_lose(word, encoded_word, lives)
    return [word, guessed_letters, lives, encoded_word, missed_letters]


def win_or_lose(word, guessed_word, lives):
    global game_state
    if (word == guessed_word) and lives != 0:
        print("You guessed the word correctly!")
        game_state = "Win"
        input()
    elif lives == 0:
        print("You lost!\nThe word was", word)
        game_state = "Lose"
        input()


def main():
    global game_state, difficulty
    settings = game_setup()
    guessed_letters = []
    missed_letters = []
    lives = settings[0]
    word = settings[1]
    key = encode_word(word)
    print(hangmandrawing(difficulty, lives))
    print(key)
    hangman(word, guessed_letters, lives, key, missed_letters)


main()


