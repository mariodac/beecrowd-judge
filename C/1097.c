// 1097 	Sequencia IJ 3
#include<stdio.h>
int main(){
    int i,j,x;
    x=0;
    for(i=1;i<=9;i+=2){
        for(j=7+x;j>=5+x;j--){
            printf("I=%d J=%d\n",i,j);
        }
   x+=2;
   }

return 0;
}