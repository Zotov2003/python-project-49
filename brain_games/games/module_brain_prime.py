import random


def prime(num):
    counter2 = 0
    res = ""
    for j in range(1, 501):
        if num % j == 0:
            counter2 += 1
        elif counter2 == 2:
            res = "yes"
        elif counter2 > 2:
            res = "no"
    return res


def main():
    num = random.randrange(1, 500)
    operation = (f"Question: {num}")
    
    res = prime(num)
    return operation, res
