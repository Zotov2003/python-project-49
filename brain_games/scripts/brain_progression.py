#!/usr/bin/env python3
import random
from brain_games import cli
def main():

    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(f"Hello, {name}!")
    counter = 0 
    print("What number is missing in the progression?")
    
    for i in range (1, 4):
        start = random.randrange(1, 10)
        step = random.randrange(1, 5)
        index = random.randrange(1, 10)
        num_res = 0
        progression = [start + step * i for i in range(10)]
        num_res = progression[index]
        progression[index] = ".."
        print("Question: ", end = "")
        print(*progression)
        input1 = input("Your answer: ")
        if input1 == str(num_res):
            print("Correct!")
            counter += 1
        else:
            print(f"'{input1}' is wrong answer ;(. Correct answer was '{num_res}'.")
            break
        if counter == 3:
            print(f"Congratulations, {name}!")
            
if __name__ == '__main__':
    main()