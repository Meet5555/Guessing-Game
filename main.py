from colorsys import hsv_to_rgb
import random
randNum = random.randint(1, 100)
# print(randNum)
guesses = 0
userGuess = None
while(userGuess != randNum):
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if(userGuess == randNum):
        print("Congrats! You guessed it Right")
    else:
        if(userGuess < randNum):
            print("Opps! You guessed it Wrong...Enter larger Number:")
        else:
            print("Opps! You guessed it Wrong...Enter smaller Number")

print(f"You guessed it right in {guesses} guess")

with open('highscore.txt') as f:
    highScore = int(f.read())

if(highScore > guesses):
    print(f"You Just Broken a record with high Score {guesses}")
    with open('highscore.txt', 'w') as f:
        f.write(str(guesses))