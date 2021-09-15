from math import sqrt

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def getTruncs(num):
    ret = [num]
    for i in range(1, len(str(num))):
        ret += [int(str(num)[:i])]
        ret += [int(str(num)[i:])]
    return ret

def check(num):
    truncations = getTruncs(num)
    for tru in truncations:
        if not isPrime(tru):
            return False
    return True

soma = 0
for num in range(10,1000001):
    if check(num):
        soma += num

print(soma)
