import random
import os

hangman = ['''
.-=-.
|   |
''', '''
  |
  |
.-=-.
|   |
''', '''
   _______
  |
  |
.-=-.
|   |
''', '''
   _______
  |       |
  |
.-=-.
|   |
''', '''
   _______
  |       |
  |       O
.-=-.
|   |
''', '''
   _______
  |       |
  |      _O
.-=-.
|   |
''', '''
   _______
  |       |
  |      _O_
.-=-.
|   |
''', '''
   _______
  |       |
  |      _O_
.-=-.     |
|   |
''', '''
   _______
  |       |
  |      _O_
.-=-.   __|
|   |
''', '''
   _______
  |       |
  |      _O_
.-=-.   __|__
|   |
''']

words = ['work',
         'lion',
         'mail',
         'pork',
         'play',
         'game',
         'frog',
         'card',
         'blue',
         'fish']


def welcome():
    """
    Function to start the game and make a choice.
    """
    print('Welcome to Hangman')
    print('Play Hangman')
    print('Choose between 1 or 2')
    print('1.Instructions')
    print('2.Play Game')
    start = input("write your answer here: ").strip()

    if start == '1':
        instructions()
    elif start == '2':
        return
    else:
        print('Incorrect! You should choose 1 or 2. Please, try again')


def instructions():
    """
    Shows how the game works.
    """
    print('===========INSTRUCTIONS====================')
    print('you have to figure out the 4 letter word')
    print('Guess a letter you have 26 letters to guess')
    print('You have only 10 chances')
    print('===========================================')
    welcome()


def validate(value):
    """
    Validate letter so that the user cannot make mistakes.
    """
    if len(value) != 1 or not value.isalpha():
        raise ValueError("Please enter a single letter.")
    return True


def play_game():
    """
    This function makes it possible to see how many chances
    you have and see if you have guessed right or wrong.
    The user receives an answer as to how many chances
    the user has left and whether the user has won or lost.
    It also says which word the user guessed.
    """
    # sets up a random name
    word = random.choice(words)
    # create set (to stop duplication) of guesses
    correct_guesses = set()
    incorrect_guesses = set()
    # sets turn amount
    turns = 10

    while turns > 0:

        failed = 0

        for letter in word:

            if letter in correct_guesses:
                print(letter, end=" ")

            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:

            print("You Win")

            print("The word is: ", word)
            play_again()
            break

        print()
        guess = input("guess a letter:").lower()

        try:
            validate(guess)
        except ValueError as ve:
            print(ve)
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            correct_guesses.add(guess)
        else:
            incorrect_guesses.add(guess)
            turns -= 1
            print(hangman[9 - turns])
            print("Wrong! You have", turns, "more guesses.")

        if turns == 0:
            print("You Lose. The word was:", word)
            play_again()
            break


def play_again():
    """
    The user has a chance to choose whether
    the user wants to play again or quit.
    """

    print('Choose one of the options:')
    print('1. Play the Game Again.')
    print('2. Game Over')
    answer = input('Enter your option here: ')

    if answer == '1':
        play_game()
    elif answer == '2':
        exit()
    else:
        print('Incorrect Please enter 1 or 2.')


def exit():
    """
    Clear the screen.
    """

    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Run all program functions.
    """
    welcome()
    play_game()
    exit()


if __name__ == "__main__"
main()