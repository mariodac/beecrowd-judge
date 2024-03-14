// 1017 	Gasto de Combustível
#include <stdio.h>
int main(){
    float Q,T,V;
    scanf("%f",&T);
    scanf("%f",&V);
    Q=(T*V)/12;
    printf("%0.3f\n",Q);
    return 0;
}