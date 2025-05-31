
#include "myfactory.h"
#include <string.h>

struct Parrot {
    PTRFUN* vtable;
    char* name;
};

char const* parrotName(void* this) {
    return ((struct Parrot*)this)->name;
}

char const* parrotGreet() {
    return "hello!";
}

char const* parrotMenu() {
    return "Seeds";
}

PTRFUN parrotVTable[3] = { parrotName, parrotGreet, parrotMenu };

void* create(char const* name) {
    struct Parrot* p = (struct Parrot*)malloc(sizeof(struct Parrot));
    p->vtable = parrotVTable;
    p->name = strdup(name);
    return p;
}
