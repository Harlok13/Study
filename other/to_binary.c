#include <stdio.h>

unsigned long long to_binary(long long num) {
    unsigned long long b = 0;
    unsigned long long i = 1;
    while (num > 0) {
        b += (num & 1) * i;
        i += 10;
        num >>= 1;
    }
    return b;
}

int main(void) {
    printf("%lld", to_binary(50));
    return 0;
}

