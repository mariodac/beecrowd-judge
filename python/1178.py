x = float(input().strip())

x = round(x, 4)
# print(f"{x:.4f}")
n = [None]*100
n[0] = x
for i in range(1, len(n)):
    x /= 2
    n[i] = x


for i in range(len(n)): print(f"N[{i}] = {n[i]:.4f}")