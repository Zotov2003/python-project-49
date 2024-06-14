#!/usr/bin/env python3
import random
from brain_games import cli


def answer(num):
    if num % 2 == 0:
        answer = "yes"
    elif num % 2 != 0:
        answer = "no"
    return answer


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    counter = 0
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(1, 4):
        num = random.randrange(1, 100)
        print(f"Question: {num}")
        input1 = input("Your answer: ")
        if input1 == answer(num):
            print("Correct!")
            counter += 1
        else:
            print(f"{input1} is wrong answer ;(. ", end="")
            print(f"Correct answer was {answer(num)}.")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
