#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int gt_int(const void *a, const void *b) {
    int *pa = (int *)a;
    int *pb = (int *)b;
    return (*pa > *pb);
}

int gt_char(const void *a, const void *b) {
    char *pa = ( char *)a;
    char *pb = ( char *)b;
    return (*pa > *pb);
}

int gt_str(const void *a, const void *b) {
    char **pa = ( char **)a;
    char **pb = ( char **)b;
    return strcmp(*pa, *pb) > 0;  //usporedba 2 stringa
}

const void* mymax(const void *base, size_t nmemb, size_t size, int (*compar)(const void *, const void *)) {
    const char *ptr = (const char *)base;
    const void *max = base;
    for (size_t i = 1; i < nmemb; i++) {
        if (compar(ptr + i * size, max))
            max = ptr + i * size;
    }
    return max;
}

int main() {
    int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
    char arr_char[] = "Suncana strana ulice";
    const char *arr_str[] = {
       "Gle", "malu", "vocku", "poslije", "kise",
       "Puna", "je", "kapi", "pa", "ih", "njise"
    };

    int max_int = *(int *)mymax(arr_int, sizeof(arr_int) / sizeof(arr_int[0]), sizeof(int), gt_int);
    char max_char = *(char *)mymax(arr_char, strlen(arr_char), sizeof(char), gt_char);
    const char *max_str = *( char **)mymax(arr_str, sizeof(arr_str) / sizeof(arr_str[0]), sizeof(const char *), gt_str);

    printf("max element u arr_int: %d\n", max_int);
    printf("max element u arr_char: %c\n", max_char);
    printf("max element u arr_str: %s\n", max_str);

    return 0;
}
