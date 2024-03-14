// 1048 	Aumento de Salário
#include <stdio.h>

int main() {
    float sl,ns,r;

    scanf("%f",&sl);

    if (sl<=400.0) {
        ns=sl*1.15;
        r=sl*1.15-sl;
        printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 15 %%\n",ns,r);
    } else if (sl <= 800.0) {
        ns=sl * 1.12;
        r=sl*1.12-sl;
        printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 12 %%\n",ns,r);
    } else if (sl <= 1200.0) {
        ns=sl*1.10;
        r=sl*1.10-sl;
        printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 10 %%\n",ns,r);
    } else if (sl <= 2000.0) {
        ns=sl*1.07;
        r=sl*1.07-sl;
        printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 7 %%\n",ns,r);
    } else {
        ns=sl*1.04;
        r=sl*1.04-sl;
        printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 4 %%\n",ns,r);
    }

    return 0;
}
