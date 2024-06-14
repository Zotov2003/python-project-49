#!/usr/bin/env python3
import random
from brain_games import cli


def action1(x1, action, x2):
    if action == "+":
        result = x1 + x2
    elif action == "-":
        result = x1 - x2
    elif action == "*":
        result = x1 * x2
    return str(result)


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    counter = 0
    for i in range(1, 4):
        arithmetic = ["+", "-", "*"]
        x1 = random.randrange(1, 10)
        x2 = random.randrange(1, 10)
        action = random.choice(arithmetic)
        print(f"Question: {x1} {action} {x2}")
        input1 = input("Your answer: ")
        if input1 == action1(x1, action, x2):
            counter += 1
            print("Correct!")
        else:
            print(f"{input1} is  wrong answer ;(. ", end="")
            print(f"Correct answer was {action1(x1, action, x2)}")
            print(f"Let's try again, {name}!")
            break
        if counter == 3:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
