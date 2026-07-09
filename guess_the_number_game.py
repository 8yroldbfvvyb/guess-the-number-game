import random

number = random.randint(1, 100)
score = 0

name = input("what is your name (this is not stored its for god mode) ")
if name == 'Ben':
    print("god mode activated the number is: " + str(number))

while True:
    guess = input("guess the number: ")
    score = score + 1
    
    if int(guess) < number:
        print("Too low")
    elif int(guess) > number:
        print("Too high")
    elif int(guess) == int(number):
        print("you guessed this number: " + str(number))
        print("this was your score: " + str(score))
        again = input("do you want to play again (y/n) ")
        if again == 'y':
            number = random.randint(1, 100)
            score = 0
            continue
        elif again == 'n':
            break
