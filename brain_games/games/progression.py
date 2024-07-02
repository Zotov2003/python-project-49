import random

CONDITION = "What number is missing in the progression?"


def get_question_and_answer():
    """The function gives a sequence of 10 numbers with a certain step
    One of the numbers is replaced with ".."
    A sequence of numbers is returned and the result"""
    start = random.randrange(1, 10)
    step = random.randrange(1, 5)
    index = random.randrange(1, 10)
    answer = 0
    progression = [start + step * i for i in range(10)]
    answer = progression[index]
    progression[index] = ".."
    progression = ' '.join(str(x) for x in progression)
    question = progression
    return question, answer
