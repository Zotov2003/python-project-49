#!/usr/bin/env python3
import random

condition = "What number is missing in the progression?"

#Фунция дает последовательность из 10 чисел с определенным шагом
#Одно из чисел заменяется на ".."
#Возвращается последовательность чисел и результат
def game():
    start = random.randrange(1, 10)
    step = random.randrange(1, 5)
    index = random.randrange(1, 10)
    res = 0
    progression = [start + step * i for i in range(10)]
    res = progression[index]
    progression[index] = ".."
    progression = ' '.join(str(x) for x in progression)
    operation = progression
    return operation, res
