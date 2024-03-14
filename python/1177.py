t = int(input().strip())

n = [None]*1000
index = 0
for i in range(len(n)):
    if index == t:
        index = 0
    n[i] = index
    index += 1
    
for i in range(len(n)): print(f'N[{i}] = {n[i]}')