# 3. Generate dictionary containing (i, i*i)

print("\n3. Generate dictionary:")

n = 5
d = {}

for i in range(1, n + 1):
    d[i] = i * i

print(d)
