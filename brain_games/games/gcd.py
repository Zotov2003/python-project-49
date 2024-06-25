import random


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


def brain_gcd():
    x1 = random.randrange(1, 20)
    x2 = random.randrange(1, 20)
    operation = x1, x2
    res = nod(x1, x2)
    return operation, res
