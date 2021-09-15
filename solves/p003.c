#include <stdio.h>
#include <math.h>

#define NUM 600851475143 

int isPrime(unsigned long long int num) {
	for (unsigned long long int i = 2; i < num / 2; i++)
		if (num % i == 0 && num != i)
			return 0;

	return 1;
}

int main(int argc, char** argv) {
	unsigned long long int num = 0;

	for (unsigned long long int i = sqrt(NUM) + 1; i > 2; i--)
		if (NUM % i == 0 && isPrime(i))
			printf("%llu\n", i);

}
