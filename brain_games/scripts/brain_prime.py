#!/usr/bin/env python3
import random
from brain_games import cli


def prime(num):
    counter2 = 0
    res = ""
    for j in range(1, 501):
        if num % j == 0:
            counter2 += 1
        elif counter2 == 2:
            res = "yes"
        elif counter2 > 2:
            res = "no"
    return res


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    counter = 0
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    for i in range(3):
        num = random.randrange(1, 500)
        print(f"Question: {num}")
        input1 = input("Your answer: ")
        if prime(num) == input1:
            print("Correct!")
            counter += 1
        else:
            print(f"'{input1}' is wrong answer ;(. ", end="")
            print(f"Correct answer was '{prime(num)}'.")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
