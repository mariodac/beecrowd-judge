#include <stdio.h>
int main(){
int x=0;
float a,b,media=0;
while(x==0){
    scanf("%f",&a);
    if(a>=0 && a<=10){
    break;
    }else{
    printf("nota invalida\n");
    }}
while(x==0){
    scanf("%f",&b);
    if(b>=0 && b<=10){
    break;
    }else{
    printf("nota invalida\n");
    }}
media=(a+b)/2;
printf("media = %.2f\n",media);
return 0;
}
