import random

CONDITION = "Find the greatest common divisor of given numbers."


def nod(x1, x2):
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

# Функция дает два числа для задания
# Заданин решается в функции nod
# Возвращает числа для задания и результат вычисления


def game():
    x1 = random.randrange(1, 20)
    x2 = random.randrange(1, 20)
    operation = (f"{x1} {x2}")
    res = nod(x1, x2)
    return operation, res
