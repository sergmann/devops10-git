#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *myenvvar=getenv("EDITOR");
    printf("The editor enviroment variable is set to %s\\n", myenvvar);
}
