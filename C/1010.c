// 1010 	Cálculo Simples
#include <stdio.h>
int main(){
    int p1,p2,q1,q2;
    float v1,v2,vt;
    scanf("%d",&p1);
    scanf("%d",&q1);
    scanf("%f",&v1);
    scanf("%d",&p2);
    scanf("%d",&q2);
    scanf("%f",&v2);
    vt=(v1*q1)+(v2*q2);
    printf("VALOR A PAGAR: R$ %.2f\n",vt);
    return 0;
}