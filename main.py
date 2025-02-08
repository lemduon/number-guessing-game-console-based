import random

tries = 1

print("Number Guessing Game! (1-20)")

number = random.randint(1, 20)
print("Number generated!")

while True:
    ans = int(input("Your guess: "))
    if ans == number:
        print(f"Correct! The number was {number}.")
        break
    elif ans > 20:
        print("Invalid Response! (+1 try count penalty)")
        tries += 1
    elif ans > number:
        print("Too high! Try Again.")
        tries += 1
    elif ans < number:
        print("Too low! Try Again.")
        tries += 1

print(f"You got it in {tries} try(tries)!")
