// 1182 	Coluna na Matriz
#include<stdio.h>
int main()
{
    char o;
    int a,i,j;
    float sum=0,n;
 
 
    scanf("%d ",&a);
    scanf("%c",&o);
    for(i=0 ; i<=11 ; i++)
    {
        for(j=0 ; j<=11 ; j++)
        {
            scanf("%f",&n);
            if(j==a)
            {
 
                sum+=n;
            }
        }
 
    }
    if (o == 'S') printf("%.1f\n", sum);
    else printf("%.1f\n", sum/12);
 
    return 0;
 
}