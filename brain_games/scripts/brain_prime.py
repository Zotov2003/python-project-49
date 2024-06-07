#!/usr/bin/env python3
import random
from brain_games import cli
def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    counter = 0 
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    for i in range(3):
        res = ""
        num = random.randrange(1, 500)
        counter2 = 0
        for j in range(1, 501):
            if num % j == 0:
                counter2 += 1
            if counter2 == 2:
                res = "yes"
            if counter2 > 2:
                res = "no"
        print(f"Question: {num}")
        input1 = input("Your answer: ")
        if res == input1:
            print("Correct!")
        else:
            print(f"'{input1}' is wrong answer ;(. Correct answer was '{res}'.")
            break
        if counter == 3:
            print(f"Congratulations, {name}!")




if __name__ == '__main__':
    main()