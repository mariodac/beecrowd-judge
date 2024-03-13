#include<stdio.h>
int main(void){
    float a , b ,c , total , media;
    int i, n;
    scanf("%d",&n);
    for(i = 1; i <= n; i++){
        scanf("%f %f %f", &a, &b, &c);
        total = a * 2.0 + b * 3.0 + c * 5.0;
        media = total / 10.0;
        printf("%.1f\n", media);
    }
    return 0;
}

