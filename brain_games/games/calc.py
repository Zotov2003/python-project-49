import random


def action1(x1, action, x2):
    if action == "+":
        result = x1 + x2
    elif action == "-":
        result = x1 - x2
    elif action == "*":
        result = x1 * x2
    return str(result)

condition = "What is the result of the expression?"

def game():
    arithmetic = ["+", "-", "*"]
    x1 = random.randrange(1, 10)
    x2 = random.randrange(1, 10)
    action = random.choice(arithmetic)
    operation = (f"{x1} {action} {x2}")
    res = action1(x1, action, x2)
    return operation, res
