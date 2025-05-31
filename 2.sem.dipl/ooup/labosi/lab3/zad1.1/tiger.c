
#include "myfactory.h"
#include <string.h>

struct Tiger {
    PTRFUN* vtable;
    char* name;
};

char const* tigerName(void* this) {
    return ((struct Tiger*)this)->name;
}

char const* tigerGreet() {
    return "wraa!";
}

char const* tigerMenu() {
    return "Meat";
}

PTRFUN tigerVTable[3] = { tigerName, tigerGreet, tigerMenu };

void* create(char const* name) {
    struct Tiger* t = (struct Tiger*)malloc(sizeof(struct Tiger));
    t->vtable = tigerVTable;
    t->name = strdup(name);
    return t;
}
