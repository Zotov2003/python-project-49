import random

CONDITION = "What is the result of the expression?"


def action(x1, symbol, x2):
    if symbol == "+":
        result = x1 + x2
    elif symbol == "-":
        result = x1 - x2
    elif symbol == "*":
        result = x1 * x2
    return str(result)

#Функция дает два числа и знак для задания
#Задание решается через функцию action
#возвращает само задание и его результат
def game():
    arithmetic = ["+", "-", "*"]
    x1 = random.randrange(1, 10)
    x2 = random.randrange(1, 10)
    symbol = random.choice(arithmetic)
    operation = (f"{x1} {symbol} {x2}")
    res = action(x1, symbol, x2)
    return operation, res
