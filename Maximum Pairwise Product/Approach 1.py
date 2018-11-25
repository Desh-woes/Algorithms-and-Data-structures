# Uses python3

n = int(input())
a = [int(x) for x in input().split()]
product = 0
for i in range(n):
    for j in range(n):
        if i != j:
            product = max(product, a[i]*a[j])

print(product)
