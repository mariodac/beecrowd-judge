// 1040 	Média 3
#include <stdio.h>
int main(){
float n1,n2,n3,n4,m,ne;
scanf("%f %f %f %f",&n1,&n2,&n3,&n4);
m=(n1*2+n2*3+n3*4+n4*1)/10;
printf("Media: %.1f\n",m);
if(m>=7.0)
    printf("Aluno aprovado.\n");
else if(m>=5.0){
    printf("Aluno em exame.\n");
    scanf("%f",&ne);
    printf("Nota do exame: %.1f\n",ne);
        if(ne+m/2>5.0)
        printf("Aluno aprovado.\n");
        else
        printf("Aluno reprovado.\n");
        printf("Media final: %.1f\n",(ne+m)/2);
        }else
        printf("Aluno reprovado.\n");
return 0;}
