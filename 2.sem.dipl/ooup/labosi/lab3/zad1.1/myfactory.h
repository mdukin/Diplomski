#ifndef MYFACTORY_H
#define MYFACTORY_H

#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

struct Animal {
    PTRFUN* vtable;
};

void* myfactory(char const* libname, char const* ctorarg);
void animalPrintGreeting(struct Animal* animal);
void animalPrintMenu(struct Animal* animal);

#endif 