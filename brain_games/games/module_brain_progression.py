#!/usr/bin/env python3
import random


def brain_progression():
    start = random.randrange(1, 10)
    step = random.randrange(1, 5)
    index = random.randrange(1, 10)
    res = 0
    progression = [start + step * i for i in range(10)]
    res = progression[index]
    progression[index] = ".."
    operation = (f"Question: {progression}")
    return operation, res
