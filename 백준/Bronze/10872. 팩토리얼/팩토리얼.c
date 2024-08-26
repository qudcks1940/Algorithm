#include <stdio.h>

int factorial(int);

int main() {
	int num;
	scanf("%d", &num);
	printf("%d", factorial(num));

	return 0;
}

int factorial(int n) {
	if (n == 0 || n == 1) {
		return 1;
	}
	return n * factorial(n - 1);
}