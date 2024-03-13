#include <stdio.h>
int main(){
int n,c;
float x,y;
scanf("%d",&n);
for(c=0;c<n;c++){
    scanf("%f %f",&x,&y);
    if(y==0){
        printf("divisao impossivel\n");
    }
    else {
    printf("%.1f\n",x/y);
    }
}
return 0;
}
