import random

CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """The is_prime function determines whether a number is prime
    Next, the function returns the result
    to the get_question_and_answer function"""
    counter = 0
    res = ""
    for j in range(1, 501):
        if num % j == 0:
            counter += 1
        elif counter == 2:
            res = True
        elif counter > 2:
            res = False
            break
    return res


def get_question_and_answer():
    """The function gives a number for the task
    The task is solved through the is_prime function
    Returns the number for the task and its result"""
    num = random.randrange(1, 500)
    question = num
    answer = "yes" if is_prime(num) else "no"
    return question, answer
