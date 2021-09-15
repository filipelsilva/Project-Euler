import math

def getSumDivisors(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0:
            sum += i
            if n/i != i:
                sum += n/i
    return sum

soma = 0

for i in range(1, 10001):
    num = getSumDivisors(i)
    if getSumDivisors(num) == i and num != i:
        soma += i

print(soma)
