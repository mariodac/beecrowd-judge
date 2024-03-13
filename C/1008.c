#include <stdio.h>
int main(){
    int NF,HT;
    float VH;
    scanf("%d",&NF);
    scanf("%d",&HT);
    scanf("%f",&VH);
    printf("NUMBER = %d\n",NF);
    printf("SALARY = U$ %0.2f\n",HT*VH);
    return 0;
}