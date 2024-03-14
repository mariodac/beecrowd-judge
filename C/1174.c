// 1174 	Seleçao em Vetor I
#include <stdio.h>
#define tam 100
int main()
{
    double A[tam];
    int i;
    for(i=0; i<tam; i++)
        scanf("%lf", &A[i]);
    for(i=0; i<tam; i++)
    {
        if(A[i]<=10.0)
            printf("A[%d] = %.1lf\n",i, A[i]);
    }
    return 0;
}