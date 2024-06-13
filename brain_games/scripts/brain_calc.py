#!/usr/bin/env python3
import random
from brain_games import cli
def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    result = 0
    counter = 0

    for i in range (1, 4):
        
        arithmetic = ["+", "-", "*"]
        x1 = random.randrange(1, 10)
        x2 = random.randrange(1, 10)
        action = random.choice(arithmetic)
        print(f"Question: {x1} {action} {x2}")
        input1 = input("Your answer: ")
        if action == "+":
            result = x1 + x2
            if input1 == str(result):
                counter += 1
                print("Correct!")
            else:
                print(f"{input1} is  wrong answer ;(. Correct answer was {result}")
                print(f"Let's try again, {name}!")
                break
        if action == "-":
            result = x1 - x2
            if input1 == str(result):
                counter += 1
                print("Correct!")
            else:
                print(f"{input1} is  wrong answer ;(. Correct answer was {result}")
                print(f"Let's try again, {name}!")
                break
        if action == "*":
            result = x1 * x2
            if input1 == str(result):
                counter += 1
                print("Correct!")
            else:
                print(f"{input1} is  wrong answer ;(. Correct answer was {result}")
                print(f"Let's try again, {name}!")
                break
        if counter == 3:
            print(f"Congratulations, {name}!")
            
if __name__ == '__main__':
    main()