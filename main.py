#Number Guessing Game Objectives:
from random import randint
from art import logo
print(logo)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def compare_number():
  global guess
  global answer
  global lives
  if guess == answer:
    print(f"You got it! The answer was {answer}.")
    return lives - 11
  elif guess > answer:
    print("Too high.")
    return lives - 1
  else:
    print("Too low.")
    return lives - 1

answer = randint(1, 100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.: ")
if difficulty == "easy":
  lives = 10
elif difficulty == "hard":
  lives = 5
else:
  print("That was not a valid answer. Please restart.")
  lives = ""
while lives > 0:
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  lives = compare_number()
if lives == 0:
  print("You've run out of guesses. You lose.")