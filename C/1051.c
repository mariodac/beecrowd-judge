#include <stdio.h>

int main() {
    float s,ir;

    scanf("%f",&s);

    if (s<=2000.0) {
        printf("Isento\n");
    } else if (s<=3000.0) {
        ir=(s-2000.0)*0.08;
        printf("R$ %.2f\n",ir);
    } else if (s<=4500.0) {
        ir=1000.0*0.08+(s-3000.0)*0.18;
        printf("R$ %.2f\n",ir);
    } else {
        ir=1000.0*0.08+1500.0*0.18+(s-4500.0)*0.28;
        printf("R$ %.2f\n",ir);
    }

    return 0;
}
