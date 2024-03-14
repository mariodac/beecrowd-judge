// 1047 	Tempo de Jogo com Minutos
#include <stdio.h>
int main()
{
    int hi,mi,hf,mf,h,m;
    scanf("%d %d %d %d",&hi,&mi,&hf,&mf);

    h=hf-hi;
    if(hf-hi<0)
        h=24+hf-hi;

    m=mf-mi;
    if(mf-mi<0){
        m=60+mf-mi;
        h--;
    }

    if(hf==hi && mf==mi){
        printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
    }else{
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n",h,m);
    }
    return 0;
}