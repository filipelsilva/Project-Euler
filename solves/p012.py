import math

def getNumDivisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1) :
        if n % i == 0:
            if n/i == i:
                count += 1
            else:
                count += 2
    return count

triangle = 0

for i in range(1, 10000000001):
    triangle += i
    if getNumDivisors(triangle) > 500:
        print(triangle)
        break
