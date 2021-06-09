import random

guessedNo = random.randint(1,20)

guessCount = 5

while (guessCount > 0):
    playerGuess = int(input("Enter your guess:"))
    if playerGuess == guessedNo:
        print("Congratulations YOU WON!!")
        print(guessedNo)
    else:
        print("YOU Lose!! Try again")


guessCount = guessCount - 1

     