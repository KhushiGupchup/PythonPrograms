#Random Number Guessing Game
import random

secret_Num = random.randint(1,10)

attempt=3

print("Thinking number between 1 to 10")

while attempt > 0 :
  guess= int(input("Make a guess"))
  if guess == secret_Num:
    print("Congrats !! you guess it write")
    break
  elif guess < secret_Num:
    print("Try again!! too low")
  else:
    print("Too high ! try again")
  attempt -=1

  if attempt == 0:
    print("Sorry, attempt are over !! the secret number was:",secret_Num)

