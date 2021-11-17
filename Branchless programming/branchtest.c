#include <stdio.h>

int Smaller(int a, int b);
int Smaller_Branchless(int a, int b);

int main(void){
    int a = 1;
    int b = 0;
    Smaller(a, b); // Smaller() will take more time than Smaller_Branchless()
    Smaller_Branchless(a, b);
    return 0;
}
int Smaller(int a, int b)
{
    if(a < b){
        return a;
    }else{
        return b;
    }
}
int Smaller_Branchless(int a, int b)
{
    return a*(a<b) + b*(b<=a);
    /* So summarising...

        a * (condition for a) + b * (condition for b) + c * (condition for c) + ...
        
    */
}