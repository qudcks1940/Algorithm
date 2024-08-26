#include <stdio.h>
#include <stdlib.h>

int fibo(int);

int main() {
	int N;

	scanf("%d", &N);
	printf("%d\n",fibo(N));



	return 0;
}

int fibo(int N) {
	
	int* array = (int*)malloc(sizeof(int) * (N+1));
	array[0] = 0;
	array[1] = 1;
	array[2] = 1;
	if (N > 1) {
		for (int i = 2; i < (N+1); i++) {
			array[i] = array[i - 2] + array[i - 1] ;
		}
	}
	
	
	int result = array[N];
	free(array);

	return result;
}