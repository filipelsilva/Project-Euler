from math import sqrt

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def getRotation(num):
    ret = []
    for i in range(len(str(num))):
        ret += [int(str(num)[i:]+str(num)[:i])]
    return ret

def check(num):
    rotations = getRotation(num)
    for rot in rotations:
        if not isPrime(rot):
            return False
    return True

count = 0
for num in range(1,1000001):
    if check(num):
        count += 1

print(count)
