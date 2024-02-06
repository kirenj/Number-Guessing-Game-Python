import random
from art import logo

NUMBER_SELECTION = random.randint(1, 100)
CONTINUE_PLAY = True

def easy_mode():
  global CONTINUE_PLAY
  #global number_selection
  lives_left = 10
  print(f"You have {lives_left} attempts remaining to guess the number.")  

  while CONTINUE_PLAY == True:
    guess = int(input("Make a guess: "))
    if guess == NUMBER_SELECTION:
      print(f"You got it!. The number was {NUMBER_SELECTION}")
      CONTINUE_PLAY = False
    elif lives_left == 1:
      print("You've run out of guesses, you lose.")
      CONTINUE_PLAY = False    
    elif guess > NUMBER_SELECTION:
      print("Too high. Guess again.")
      lives_left -= 1
      print(f"You have {lives_left} attempts remaining to guess the number.")      
    elif guess < NUMBER_SELECTION:
      print("Too low. Guess again.")
      lives_left -= 1
      print(f"You have {lives_left} attempts remaining to guess the number.")


def hard_mode():
  global CONTINUE_PLAY
  lives_left = 5
  print(f"You have {lives_left} attempts remaining to guess the number.")  

  while CONTINUE_PLAY == True:
    guess = int(input("Make a guess: "))
    if guess == NUMBER_SELECTION:
      print(f"You got it!. The number was {NUMBER_SELECTION}")
      CONTINUE_PLAY = False
    elif lives_left == 1:
      print("You've run out of guesses, you lose.")
      CONTINUE_PLAY = False    
    elif guess > NUMBER_SELECTION:
      print("Too high. Guess again.")
      lives_left -= 1
      print(f"You have {lives_left} attempts remaining to guess the number.")      
    elif guess < NUMBER_SELECTION:
      print("Too low. Guess again.")
      lives_left -= 1
      print(f"You have {lives_left} attempts remaining to guess the number.")
      

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  
  
  
  print(NUMBER_SELECTION)
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()      
  
  
  if difficulty == 'easy':
    easy_mode()
  elif difficulty == 'hard':
    hard_mode()
  else:
    print("You have entered an incorrect input.")


game()