def merge_sort(arr):
    merge_sort2(arr, 0, len(arr)-1)


def merge_sort2(arr, first, last):
    if first < last:
        middle_index = (first+last)//2
        merge_sort2(arr, first, middle_index)
        merge_sort2(arr, middle_index+1, last)
        merge(arr, first, middle_index+1, last)


def merge(arr, first, middle, last):
    left_list = arr[first:middle]
    right_list = arr[middle:last+1]
    left_list.append(999999999)
    right_list.append(999999999)
    i = j = 0
    for k in range(first, last+1):
        if left_list[i] <= right_list[j]:
            arr[k] = left_list[i]
            i += 1

        else:
            arr[k] = right_list[j]
            j += 1


# Test parameters
arr_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
merge_sort(arr_test)
print(arr_test)