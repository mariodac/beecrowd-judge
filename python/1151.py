# 1151 - Fibonacci Fácil 

n = int(input())
fib = []

prev1 = 0
prev2 = 1
print(f'{prev1}',  end=' ')
i = 2
while i <= n:
    next = prev1 + prev2
    prev2 = prev1
    prev1 = next
    if i >= n:
        print(f'{next}')
    else:
        print(f'{next}', end=' ')
    i += 1