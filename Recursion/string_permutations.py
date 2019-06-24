def permutations(main_str):
    results = []
    _permutations_helper("", main_str, results)
    return results


def _permutations_helper(prefix_str, suffix_str, results_arr):
    # Define the base case
    if len(suffix_str) == 0:
        results_arr.append(prefix_str)
    else:
        # Recursive call
        # go through all the characters in the suffix array
        for i in range(len(suffix_str)):
            _permutations_helper(prefix_str+suffix_str[i], suffix_str[0:i]+suffix_str[i+1:], results_arr)


print(len(permutations("1234567")))
