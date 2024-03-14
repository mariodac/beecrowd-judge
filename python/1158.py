n = int(input())
odds = 0
soma = 0
for _ in range(n):
    x, y = map(int, input().strip().split(' '))
    i = x
    while odds < y:
        if i % 2 != 0:
            soma += i
            odds += 1
        i += 1
    print(soma)
    odds = 0
    soma = 0