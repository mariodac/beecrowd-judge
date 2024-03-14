// 1080 	Maior e Posição
#include <stdio.h>
int main()
{
    int c, p, m, n;
    c = 0; p = 0;
    for(c = 1; c <= 100; c++){
        scanf("%d", &n);
        if(m < n){
            m = n;
            p = c;
        }
    }
printf("%d\n%d\n", m, p);
return 0;
}
