import random

CONDITION = "Answer \"yes\" if given number is prime. "
CONDITION += "Otherwise answer \"no\"."


def calculating_prime(num):
    counter = 0
    res = ""
    for j in range(1, 501):
        if num % j == 0:
            counter += 1
        elif counter == 2:
            res = "yes"
        elif counter > 2:
            res = "no"
    return res


def get_question_and_answer():
    """The function gives a number for the task
    The task is solved through the calculating_prime function
    Returns the number for the task and its result"""
    num = random.randrange(1, 500)
    question = num
    answer = calculating_prime(num)
    return question, answer
