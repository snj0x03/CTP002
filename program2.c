#include <stdio.h>

int main() {
    int x;
    printf("Enter the two integers: ");
    scanf("%d", &x);

    printf("Printed using %%d: %d\n", x);
    printf("Printed using %%i: %3i\n", x);
    return 0;
}