from math import sqrt

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def getPrimes(limit):
    primes = [2,3]
    for i in range(1, limit//6 + 1):
        n1 = 6 * i - 1
        n2 = 6 * i + 1
        if n1 >= limit and n2 >= limit:
            return primes
        if n1 < limit and isPrime(n1):
            primes.append(n1)
        if n2 < limit and isPrime(n2):
            primes.append(n2)
    return primes

LIMIT = 1000000

soma = 0
maxi = 0
maxilen = 0

primes = getPrimes(LIMIT)
set_primes = set(primes)

for i in range(len(primes)):
    soma = 0
    for j in range(i, len(primes)):
        soma += primes[j]
        length = j - i + 1
        if soma < LIMIT and soma in set_primes:
            if length > maxilen or (length == maxilen and soma > maxi):
                maxilen = length
                maxi = soma

print(maxi, maxilen)
