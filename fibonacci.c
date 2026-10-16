#include <stdio.h>

int main(void) {
    int n, i;
    long long first = 0, second = 1, next;

    printf("Enter the number of terms: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    printf("Fibonacci series: ");
    for (i = 0; i < n; i++) {
        printf("%lld", first);
        if (i < n - 1) {
            printf(" ");
        }
        next = first + second;
        first = second;
        second = next;
    }

    printf("\n");
    return 0;
}
