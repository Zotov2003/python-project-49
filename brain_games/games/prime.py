import random

CONDITION = "Answer \"yes\" if given number is prime. "
CONDITION += "Otherwise answer \"no\"."


def prime(num):
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

#Функция дает число для задания
#Задание решается через функцию prime
#Возвращает число для задания и его результат
def game():
    num = random.randrange(1, 500)
    operation = num
    res = prime(num)
    return operation, res
