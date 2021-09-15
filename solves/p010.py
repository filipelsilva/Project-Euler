from math import sqrt

def isPrime(num):
	for i in range(2, int(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

soma = 5

for i in range(1,333334):
	n1 = 6 * i + 1
	n2 = 6 * i - 1
	if isPrime(n1):
		soma += n1
	if isPrime(n2):
		soma += n2

print(soma)