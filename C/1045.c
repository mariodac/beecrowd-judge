// 1045 	Tipos de Triângulos
#include <stdio.h>

int main() {
    double a, b, c, d;
    scanf("%lf %lf %lf", &a, &b, &c);

    if (a < b) { 
        d = a; 
        a = b; 
        b = d; }
    if (b < c) { 
        d = b; 
        b = c; 
        c = d; }
    if (a < b) { 
            d = a;
        a = b; 
        b = d; }

    if (a >= b + c) printf("NAO FORMA TRIANGULO\n");
        else if (a * a == b * b + c * c) 
            printf("TRIANGULO RETANGULO\n");
        else if (a * a > b * b + c * c) 
            printf("TRIANGULO OBTUSANGULO\n");
        else if (a * a < b * b + c * c) 
            printf("TRIANGULO ACUTANGULO\n");

    if (a == b && b == c) printf("TRIANGULO EQUILATERO\n");
        else if (a == b || b == c) printf("TRIANGULO ISOSCELES\n");

    return 0;
}