# Uses python3
x = 3
y = [1, 2, 3]

z = max(y)
for items in range(x):
    for item in range(0, len(y)):
        if items != z:
            if y[items] > y[item]:
                print(y[items])
