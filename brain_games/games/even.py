import random

CONDITION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_even(num):
    """The is_even function checks whether the passed number is even
    Next, it returns the result to the get_question_and_answer function"""
    if num % 2 == 0:
        answer = True
    elif num % 2 != 0:
        answer = False
    return answer


def get_question_and_answer():
    """the function outputs a number to solve the task
    the calculating_even_number function finds the correct answer
    returns the number itself for the task and its result"""
    num = random.randrange(1, 100)
    question = num
    answer = "yes" if is_even(num) else "no"
    return question, answer
