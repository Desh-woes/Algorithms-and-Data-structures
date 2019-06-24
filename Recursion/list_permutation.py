def list_permutation(items_arr):
    result_arr = []
    _list_permutation_helper(items_arr, 0, result_arr)
    return result_arr


def _list_permutation_helper(items_arr, start_index, results_arr):
    # define base case
    if start_index >= len(items_arr):
        results_arr.append(items_arr.copy())
    else:
        for i in range(start_index, len(items_arr)):
            _swap_helper_function(items_arr, start_index, i)
            _list_permutation_helper(items_arr, start_index+1, results_arr)
            _swap_helper_function(items_arr, start_index, i)


def _swap_helper_function(arr, index_i, index_j):
    temp = arr[index_i]
    arr[index_i] = arr[index_j]
    arr[index_j] = temp


print(list_permutation([1, 2, 3]))
