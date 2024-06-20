#!/usr/bin/env python3
import random
from brain_games import cli


def brain_progression():
        start = random.randrange(1, 10)
        step = random.randrange(1, 5)
        index = random.randrange(1, 10)
        num_res = 0
        progression = [start + step * i for i in range(10)]
        res = progression[index]
        progression[index] = ".."
        operation = (f"Question: {progression}", end="")
        input1 = input("Your answer: ")
        return operation, input1, res


if __name__ == '__main__':
    main()
