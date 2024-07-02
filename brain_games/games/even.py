import random

CONDITION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def calculating_even_number(num):
    if num % 2 == 0:
        answer = "yes"
    elif num % 2 != 0:
        answer = "no"
    return answer


def task_regeneration_even():
    """the function outputs a number to solve the task
    the calculating_even_number function finds the correct answer
    returns the number itself for the task and its result"""
    num = random.randrange(1, 100)
    question = num
    answer = calculating_even_number(num)
    return question, answer
