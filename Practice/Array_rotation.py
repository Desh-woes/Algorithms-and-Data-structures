# Approach 1

# Sample array
arr = [1, 2, 3, 4, 5, 6, 7]

# Number of times we want to rotate the array
rotate_value = 2

# Approach rotates values one at a time. This is quite inefficient as it makes the runtime O(k*n)// I am yet to find a
# more efficient approach
for x in range(0, rotate_value):
    temp = arr[len(arr) - 1]
    y = len(arr) - 2

    for items in range(0, len(arr)):

        if items != len(arr) - 1:
            arr[y+1] = arr[y]
            y -= 1

        elif items == len(arr) - 1:
            arr[0] = temp

print(arr)

