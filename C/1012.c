// 1012 	Área
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
    double a, b, c, pi = 3.14159, aTriangulo, aCirculo, aTrapezio, aQuadrado, aRetangulo;
    scanf("%lf %lf %lf", &a, &b, &c);
    aTriangulo = (a * c) / 2;
    aCirculo = pi * pow(c,2);
    aTrapezio = ((a + b) * c) / 2;
    aQuadrado = pow(b, 2);
    aRetangulo = a * b;
    printf("TRIANGULO: %.3f\n", aTriangulo);
    printf("CIRCULO: %.3f\n", aCirculo);
    printf("TRAPEZIO: %.3f\n", aTrapezio);
    printf("QUADRADO: %.3f\n", aQuadrado);
    printf("RETANGULO: %.3f\n", aRetangulo);
    return 0;
}
