#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    char a[8] = "0123456", b[8];

    printf("before a[]=<%s>\n", a);
    strcpy(b,"00000000abcdefg");

    printf("after a[]=<%s>\n", a);
    return 0;
}