input = [4, 3, 5, 200, 5, 3]


def find_max_subset(input_arr, output_arr):
    for i in range(0, len(input_arr)):
        if i in (0, 1):
            output_arr[i] = max(input_arr[:i+1])
            continue

        output_arr[i] = max(output_arr[i-1], output_arr[i-2]+input_arr[i])
    return max(output_arr[-1], output_arr[-2])


output = [None] * (len(input))
print(find_max_subset(input, output))
