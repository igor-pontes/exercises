#include <assert.h>
#include <dynamicarray.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void initArray(Array* a, size_t size){
	assert(size>0);
	a->array = malloc(size * sizeof(int *));
	a->size = size;
	a->used = 0;
}

void insertArray(Array* a, const char* s){
	
	if(a->used > a->size){
		a->size++;
		a->array = realloc(a->array, a->size * sizeof(int *));
	}
	size_t len = strlen(s) + 1;
	a->array[a->used] = (long int) malloc(len * sizeof(char));

	strncpy((char *)a->array[a->used++], s, len);
}

void clearArray(Array* a){
	
	for (int i = 0; i < a->used; i++){
		free((void *)a->array[i]);
	}
	free((void *)a->array);
	a->array = NULL;
	a->used = a-> size = 0;
}

