# 1150 - Ultrapassando Z 

x = int(input())
z = x - 1
while z <= x:
    z = int(input())
numbers = 0
seq = x
greater = 0

while greater <= z:
    if numbers == 0:
        greater += x + (seq + 1)
        numbers += 2
    else:
        greater += seq
        numbers += 1
    seq += 1
    
print(numbers)
    

