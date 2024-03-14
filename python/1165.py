n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    divisor = 0
    for num in range(1, x+1):
        if x % num == 0:
            divisor += 1
    if divisor == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')