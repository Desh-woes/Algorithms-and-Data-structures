# Approach 1
# Define test arrays
# arr_1 = ['', '']
# arr_2 = ['', 'a']
#
#
# # Define function to check if the two arrays of characters are permutations of one another
# def check_arr(arr1, arr2):
#     if len(arr1) != len(arr2):
#         return False
#     else:
#         arr2 = set(arr2)
#         for items in arr1:
#             if items not in arr2:
#                 return False
#         return True
#
#
# print(check_arr(arr_1, arr_2))

# Approach 2
# Define test arrays
arr_1 = ['r', 'a', 'u', 'd', 'a']
arr_2 = ['a', 'u', 'd', 'a', 'r']


# Define a function to check if array two is a permutation of array 1
def check_arr(arr1, arr2):

    # A permutation element must have the same size
    if len(arr1) != len(arr2):
        return False

    # sort the list and check if all elements are the same
    else:
        arr1.sort()
        arr2.sort()

        # Use while loop
        iterator = 0
        while iterator < len(arr1):
            if arr1[iterator] != arr2[iterator]:
                return False
            iterator += 1

        # Return true if all values are equal
        return True


print(check_arr(arr_1, arr_2))



