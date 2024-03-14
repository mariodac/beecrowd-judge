#include<stdio.h>
int main()
{
   long long int n, p = 0, s = 1, px, c;
   int i,j;
   scanf("%d", &j);
   for(i=1; i<=j; i++, p = 0, s = 1)
   {
       scanf("%lld",&n);
       n=n+1;
       for ( c = 0 ; c < n ; c++ )
       {
          if (c <= 1) px = c;
          else
          {
             px = p + s;
             p = s;
             s = px;
          }
       }
          printf("Fib(%lld) = %lld\n",n-1,px);
   }
   return 0;
}