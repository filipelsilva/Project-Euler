import math

def getSumDivisors(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0:
            sum += i
            if n/i != i:
                sum += n/i
    return sum

# Get abundant numbers
abundant = set()
for i in range(1, 28123):
    num = getSumDivisors(i)
    if num > i:
        abundant.add(i)

print("abundant done")

numbers = set(range(1,28123))

sums = set()
for i in abundant:
    for j in abundant:
        tmp = i+j
        if tmp < 28123:
            sums.add(tmp)

print("combinations done")

notInSums = numbers - sums

soma = 0

for el in notInSums:
    soma += el

print(soma)
