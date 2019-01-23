# Approach 1
# Define test arrays
arr_1 = ['', '']
arr_2 = ['', 'a']


# Define function to check if the two arrays of characters are permutations of one another
def check_arr(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    else:
        arr2 = set(arr2)
        for items in arr1:
            if items not in arr2:
                return False
        return True


print(check_arr(arr_1, arr_2))