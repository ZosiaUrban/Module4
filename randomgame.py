import random

num1 = random.randint(1,11)


while True:
    num2 = int(input("Enter a number: "))

    if num1 == num2:
        print("YOU WON THE GAME")
        break
    elif num2 > num1:
        print("Too high")
    else:
        print("Too low")