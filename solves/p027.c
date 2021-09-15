#include <stdio.h>
#include <math.h>

int isPrime(int num) {
	if (num <= 1)
		return 0;

	for (int i = 2; i < (int) sqrt(num) + 1; i++)
		if (num % i == 0)
			return 0;

	return 1;
}

int formula(int a, int b, unsigned int n) {
	return (int) pow(n, 2) + a * n + b;
}

int consecutiveValues(int a, int b) {
	int n = 0;

	while (isPrime(formula(a, b, n)))
		n++;

	return n;
}

int main() {
	int max = 0, A = 0, B = 0, tmp = 0;

	for (int a = -1000; a <= 1000; a++) {
		for (int b = -1000; b <= 1000; b++) {
			tmp = consecutiveValues(a, b);
			if (tmp > max) {
				max = tmp;
				A = a;
				B = b;
			}
		}
	}

	printf("%d * %d = %d\n", A, B, A * B);
}
