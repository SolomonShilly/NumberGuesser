import random

def guess_number(guess):
  randomNumber = random.randint(1, 100)
  if randomNumber == guess:
    print('Congratulations! You guessed the right number!!')
    return
  else:
    print("Sorry, you did not guess the number. Would you like to try again?")
    answer = input("Enter Y for yes or N for no").lower()
    if answer == "n":
      return print("Thanks for playing!")
    while answer == "y":
      guess = int(input("Ready for your next try? Guess a number between 1 and 100! "))
      if randomNumber == guess:
            print('Congratulations! You guessed the right number!!')
            return
      else:
            print("Sorry, you did not guess the number. Would you like to try again?")
            answer = input("Enter Yes or No").lower()

print("Welcome to the number guessing game\nPlease guess a number between 1 and 100 ")
guess = int(input())
guess_number(guess)
