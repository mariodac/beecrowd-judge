// 1018 	Cédulas
#include <stdio.h>

int main (void){

    int valor = 0;
    scanf ("%d", &valor);
    printf ("%d\n",valor);

    int cedulas = ( valor - (valor%100))/100;
    printf ("%d nota(s) de R$ 100,00\n", cedulas);
    valor = valor%100 ;

    cedulas = ( valor - (valor%50))/50;
    printf ("%d nota(s) de R$ 50,00\n", cedulas);
    valor = valor%50 ;

    cedulas = ( valor - (valor%20))/20;
    printf ("%d nota(s) de R$ 20,00\n", cedulas);
    valor = valor%20 ;

    cedulas = ( valor - (valor%10))/10;
    printf ("%d nota(s) de R$ 10,00\n", cedulas);
    valor = valor%10 ;

    cedulas = ( valor - (valor%5))/5;
    printf ("%d nota(s) de R$ 5,00\n", cedulas);
    valor = valor%5 ;

    cedulas = ( valor - (valor%2))/2;
    printf ("%d nota(s) de R$ 2,00\n", cedulas);
    valor = valor%2 ;


    printf ("%d nota(s) de R$ 1,00\n", valor);


    return 0;
}