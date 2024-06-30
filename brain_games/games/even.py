import random

CONDITION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def answer(num):
    if num % 2 == 0:
        answer = "yes"
    elif num % 2 != 0:
        answer = "no"
    return answer

#функция выдает число для решения задания
#правильный ответ находит функция answewr
#возвращает само число для задания и его результат
def game():
    num = random.randrange(1, 100)
    operation = num
    res = answer(num)
    return operation, res
