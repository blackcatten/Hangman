import random
import os

hangman = ['''
.-=-.      
|   |
''',
'''
  |       
  |       
.-=-.      
|   |
''',
'''
   _______
  |       
  |      
.-=-.      
|   |
''',
'''
   _______
  |       |
  |      
.-=-.      
|   |
''',
'''
   _______
  |       |
  |       O
.-=-.     
|   |
''',
'''
   _______
  |       |
  |      _O 
.-=-.     
|   |
''',
'''
   _______
  |       |
  |      _O_ 
.-=-.     
|   |
''',
'''
   _______
  |       |
  |      _O_ 
.-=-.     | 
|   |
''',
'''
   _______
  |       |
  |      _O_ 
.-=-.   __| 
|   |     
''',
'''
   _______
  |       |
  |      _O_ 
.-=-.   __|__ 
|   |    
''']

words = ['work', 'lion', 'mail', 'pork', 'play', 'game', 'frog', 'card', 'blue', 'fish']

word = random.choice(words)

correct_guesses = set()
incorrect_guesses = set()

turns = 10

def play_game():
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
          break

      print()
      guess = input("guess a letter:").lower()
  
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
          break

def main_menu():
  play_game()

main_menu():