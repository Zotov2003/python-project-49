import random


def answer(num):
    if num % 2 == 0:
        answer = "yes"
    elif num % 2 != 0:
        answer = "no"
    return answer


def brain_even():
    num = random.randrange(1, 100)
    operation = (f"Question: {num}")
    input1 = input("Your answer: ")
    res = answer(num)
    return operation, input1, res

