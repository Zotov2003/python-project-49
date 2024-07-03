import random

CONDITION = "What is the result of the expression?"


def calculate(x1, symbol, x2):
    """The calculate function calculates the result of the expression
    Next, the result is passed to the get_question_and_answer function"""
    if symbol == "+":
        result = x1 + x2
    elif symbol == "-":
        result = x1 - x2
    elif symbol == "*":
        result = x1 * x2
    return result


def get_question_and_answer():
    """The function gives two numbers and a sign for the task
    The task is solved through the calculating_the_result function
    Returns the task itself and its result"""
    signs = ["+", "-", "*"]
    x1 = random.randrange(1, 10)
    x2 = random.randrange(1, 10)
    symbol = random.choice(signs)
    question = f"{x1} {symbol} {x2}"
    answer = calculate(x1, symbol, x2)
    return question, answer
