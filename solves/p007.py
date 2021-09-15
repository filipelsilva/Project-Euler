from math import sqrt

def isPrime(num):
	for i in range(2, int(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

i = 1
count = 2

while True:
	n1 = 6 * i + 1
	n2 = 6 * i - 1
	i += 1
	if isPrime(n1):
		count += 1
		if count == 10001:
			print(n1)
			break
	if isPrime(n2):
		count += 1
		if count == 10001:
			print(n2)
			break