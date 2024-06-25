import random


def answer(num):
    if num % 2 == 0:
        answer = "yes"
    elif num % 2 != 0:
        answer = "no"
    return answer


def brain_even():
    num = random.randrange(1, 100)
    operation = num
    res = answer(num)
    return operation, res
