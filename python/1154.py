# 1154 - Idades
ages = []
age = 1
while age > 0:
    age = int(input())
    if age > 0:
        ages.append(age)
        
print(f'{(sum(ages)/len(ages)):.2f}')