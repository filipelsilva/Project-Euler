#include <stdio.h>

#define CEIL 1000

int main(int argc, char** argv) {
	int soma = 0;

	for (int i = 0; i < CEIL; i++)
		if (i % 3 == 0 || i % 5 == 0)
			soma += i;

	printf("%d\n", soma);
}
