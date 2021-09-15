#include <stdio.h>

#define CEIL 4000000

int main(int argc, char** argv) {
	int soma = 0, num = 1, prev = 0;

	do {
		num += prev;
		prev = num - prev;
		
		if (num % 2 == 0) {
			soma += num;
		}

	} while (num <= CEIL);

	printf("%d\n", soma);
}
