import random

CONDITION = "Find the greatest common divisor of given numbers."


def calculating_nod(x1, x2):
    res = 0
    if x1 < x2:
        for j in range(1, x1 + 1):
            if x1 % j == 0 and x2 % j == 0:
                res = j
    else:
        for j in range(1, x2 + 1):
            if x1 % j == 0 and x2 % j == 0:
                res = j
    return str(res)


def get_question_and_answer():
    """The function creates two numbers for the task
    The task is solved in the calculating_nod function
    Returns the numbers for the task and the result of the calculation"""
    x1 = random.randrange(1, 20)
    x2 = random.randrange(1, 20)
    question = (f"{x1} {x2}")
    answer = calculating_nod(x1, x2)
    return question, answer
