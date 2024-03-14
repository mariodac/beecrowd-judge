// 1009 	Salário com Bônus
#include <stdio.h>
int main() {
char NOME;
double S,TV,ST;
scanf("%s", &NOME);
scanf("%lf",&S);
scanf("%lf",&TV);
ST=S+(TV*15)/100;
printf("TOTAL = R$ %0.2f\n",ST);
return 0;
}
