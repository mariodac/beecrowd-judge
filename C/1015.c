#include <stdio.h>
#include <math.h>

int main(){
    float pontos[3], distancia;
    scanf("%f", &pontos[0]);
    scanf("%f", &pontos[1]);
    scanf("%f", &pontos[2]);
    scanf("%f", &pontos[3]);
    distancia = sqrt((pow((pontos[2] - pontos[0]), 2) + pow((pontos[3] - pontos[1]), 2)));
    printf("%.4f\n", distancia);
    return 0;
}