// 1173 	Preenchimento de Vetor I    
#include <stdio.h>
int main() {
int n, i;
scanf("%d", &n);
for (i = 0; i < 10; i++) {
    printf("N[%d] = %d\n", i, n);
    n *= 2;
}

return 0;
}
