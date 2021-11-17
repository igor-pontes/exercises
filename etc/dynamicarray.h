#include <strings.h>

typedef struct { 
	long int* array;
	size_t used;
	size_t size;
} Array;

void initArray(Array* a, size_t size);

void insertArray(Array* a, const char* s);

void clearArray(Array* a);
