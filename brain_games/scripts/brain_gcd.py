#!/usr/bin/env python3
import random
from brain_games import cli


def nod(x1, x2):
    res = 0
    if x1 < x2:
        for j in range(1, x1 + 1):
            if x1 % j == 0 and x2 % j == 0:
                res = j
    else:
        for j in range(1, x2 + 1):
            if x1 % j == 0 and x2 % j == 0:
                res = j
    return str(res)


def main():

    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    counter = 0
    for i in range(1, 4):
        print("Find the greatest common divisor of given numbers.")
        x1 = random.randrange(1, 20)
        x2 = random.randrange(1, 20)
        print(f"Question: {x1} {x2}")
        input1 = input("Your answer: ")
        if input1 == nod(x1, x2):
            print("Correct!")
            counter += 1
        else:
            print(f"{input1} is wrong answer ;(. ", end="")
            print(f"Correct answer was {nod(x1, x2)}.")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
