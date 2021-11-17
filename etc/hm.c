#include <stdio.h>
#include <string.h>
#include <dynamicarray.h>

int main()
{
 char y; 
 int i=0, c=0;
 Array arr;
 initArray(&arr, 1);
 while(c<2){
	char K[20];
	int x=0;
 	fgets(&K[0], 11, stdin);
	getchar();
 	for(i=0;K[i]!='\0';i++)
	{
	        if(K[i]>='A' && K[i]<='Z'){
        		if(K[i]==y) { 
				x = 0;
               			break; 
	        	}
			x = 1;
        		y=K[i];

		}
		else{
			x = 0;
			break;
		}
	}
	if(strlen(K)<10 || strlen(K)>10)
	{
		x = 0;
	}
	if(x=1){
		insertArray(&arr, &K[0]);
		c++;
	}
	
 }
 
 printf("Strings válidas: %d \n", c);
 
 for(int u = 0;u < arr.used;u++){
 	printf("%s\n", (char *)arr.array[u]);
 }
 clearArray(&arr);
 return 0;
}
