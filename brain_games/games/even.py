import random


def answer(num):
    if num % 2 == 0:
        answer = "yes"
    elif num % 2 != 0:
        answer = "no"
    return answer

condition = "Answer \"yes\" if the number is even, otherwise answer \"no\"."

def game():
    num = random.randrange(1, 100)
    operation = num
    res = answer(num)
    return operation, res
