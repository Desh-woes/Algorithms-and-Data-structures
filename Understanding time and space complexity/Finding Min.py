# O(n^2) approach to finding the minimum value in a list
def find_min(arr):
    min_found = False
    i = 0

    while not min_found:
        min_found = True
        for x in range(0, len(arr)):
            if arr[x] < arr[i]:
                min_found = False
        i += 1
    return arr[i-1]


# Test arrays
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000, 0, -10000, 20]
print(find_min(test))


# O(n) approach to finding the minimum value in a list
def find_min2(arr):
    min_index = 0

    for x in range(1, len(arr)):
        if arr[x] < arr[min_index]:
            min_index = x
    return arr[min_index]


# Test arrays
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000, 0, -10000, 20]
print(find_min2(test))