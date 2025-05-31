#include <iostream>
#include <cstring>
#include <vector>
#include <set>

template <typename Iterator, typename Predicate>
Iterator mymax(Iterator first, Iterator last, Predicate pred) {
    if (first == last) 
        return last;

    Iterator max = first;
    ++first;
    for (; first != last; ++first) {
        if (pred(*first, *max))
            max = first;
    }
    return max;
}

int gt_int(int a, int b)
{
    return a > b ;
}

int gt_char(char a, char b)
{
    return a > b ;
}

int gt_str(const char *a, const char *b)
{
    return strcmp(a, b) > 0 ;
}


int main() {

    int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
    const int *maxint = mymax(&arr_int[0], &arr_int[sizeof(arr_int) / sizeof(*arr_int)], gt_int);
    std::cout << "Max int: " << *maxint << std::endl;

    char arr_char[] = "Suncana strana ulice";
    const char *maxchar = mymax(&arr_char[0], &arr_char[sizeof(arr_char) / sizeof(*arr_char)], gt_char);
    std::cout << "Max char: " << *maxchar << std::endl;

    const char *arr_str[] = {
       "Gle", "malu", "vocku", "poslije", "kise",
       "Puna", "je", "kapi", "pa", "ih", "njise"
    };
    const char **maxstring = mymax(&arr_str[0], &arr_str[sizeof(arr_str) / sizeof(*arr_str)], gt_str);
    std::cout << "Max cstring: " << *maxstring << std::endl;


    std::vector<int> intvector{1, 3, 5, 7, 4, 6, 9, 2, 0};
    std::set<int> intset{1, 3, 5, 7, 4, 6, 9, 2, 0};

    std::vector<int>::iterator vector_max = mymax(intvector.begin(), intvector.end(), gt_int);
    std::set<int>::iterator set_max = mymax(intset.begin(), intset.end(), gt_int);

    std::cout << "Max vector<int>: " << *vector_max << std::endl;
    std::cout << "Max set<int>: " << *set_max << std::endl;
    return 0;
}