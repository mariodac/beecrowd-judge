// 1096 	Sequencia IJ 2
#include<stdio.h>
int main(void){
    int i,j;
    for(i=1;i<=9;i+=2){
        for(j=7;j>=5;j--)
            printf("I=%d J=%d\n",i,j);
    }
    return 0;
}