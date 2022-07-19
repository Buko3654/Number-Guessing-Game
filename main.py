from random import randint
from art import logo
print(logo)

#Creates a function to compare numbers and adjust lives accordingly
def compare_number():
  #imports variables from global namespace
  global guess
  global answer
  global lives
  if guess == answer:
    print(f"You got it! The answer was {answer}.")
    #reduces lives to below where anything else will happen. ends game
    return lives - 11
  elif guess > answer:
    print("Too high.")
    return lives - 1
  else:
    print("Too low.")
    return lives - 1

#Chooses the answer between 1 and 100
answer = randint(1, 100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
#Sets the difficulty and therefore the number of lives below
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.: ")
if difficulty == "easy":
  lives = 10
elif difficulty == "hard":
  lives = 5
#in case they had a typo or gave a bad answer
else:
  print("That was not a valid answer. Please restart.")
  #sets lives to something that won't trigger game or loss scenarios
  lives = -1
#allows for repeating for the set number of chances
while lives > 0:
  print(f"You have {lives} attempts remaining to guess the number.")
  #make sure to put int to make the str an int
  guess = int(input("Make a guess: "))
  #must set the output to a variable, in this case replacing lives with new number
  lives = compare_number()
#loss scenario trigger
if lives == 0:
  print("You've run out of guesses. You lose.")