
#include "myfactory.h"
#include <dlfcn.h>

void* myfactory(char const* libname, char const* ctorarg) {
 
    char fullLibName[128];
    snprintf(fullLibName, sizeof(fullLibName), "./%s.so", libname);

    void* handle = dlopen(fullLibName, RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "Failed to open library: %s\n", dlerror());
        return NULL;
    }

    void* (*create)(char const*) = dlsym(handle, "create");
    if (!create) {
        fprintf(stderr, "Failed to load symbol create: %s\n", dlerror());
        dlclose(handle);
        return NULL;
    }

    void* animal = create(ctorarg);
    if (!animal) {
        fprintf(stderr, "Creation of animal failed.\n");
    }

    return animal;
}

