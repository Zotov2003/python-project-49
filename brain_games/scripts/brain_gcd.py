#!/usr/bin/env python3
import random
from brain_games import cli
def main():

    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    counter = 0 
    res = 0
    for i in range (1, 4):
        print("Find the greatest common divisor of given numbers.")
        x1 = random.randrange(1, 100)
        x2 = random.randrange(1, 100)
        print(f"Question: {x1} {x2}")
        input1 = input("Your answer: ")
        if x1 < x2:
            for j in range(1, x1 + 1):
                if x1 % j == 0 and x2 % j == 0:
                    res = j
        elif x2 < x1:
            for j in range(1, x2 + 1):
                if x1 % j == 0 and x2 % j == 0:
                    res = j
        if str(res) == input1:
            print("Correct!")
            counter += 1
        else:
            print(f"{input1} is wrong answer ;(. Correct answer was {res}.\nLet's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()