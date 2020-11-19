#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

enum {dump_size = 17, num_size = 4};

int main() {
    uint32_t x, num=0, s=0, shift = dump_size;

    while (scanf("%x", &x) == 1) {
        if (shift == 0) {
            shift = dump_size;
            s = 0;
            num = 0;
        }
        if (shift < dump_size) {
            x <<= (num_size - 1 - s) * 8;
            num += x;
            ++s;
            if (s == num_size) {
                printf("%" PRIu32 "\n", num);
                s = 0;
                num = 0;
            }
        }
        --shift;
    }
}
