# Approach 1 -- Passed 16 of 17 test cases. Time limit exceeded on the 17th case hence, runtime of the program needs
# to be optimised

arr = [1, 2, 3, 4]


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output_list = []
        temp_value = 1

        for x in range(0, len(nums)):
            if x == 0:
                temp_arr = nums[x + 1: len(nums)]
                for y in range(0, len(temp_arr)):
                    temp_value = temp_value * temp_arr[y]
                output_list.append(temp_value)
                temp_value = 1

            elif x > 0:
                temp_arr_right = nums[x + 1: len(nums)]
                temp_arr_left = nums[0: x]

                if len(temp_arr_left) >= len(temp_arr_right):
                    for y in range(0, len(temp_arr_left)):
                        if y <= len(temp_arr_right) - 1:
                            temp_value = temp_arr_right[y] * temp_arr_left[y] * temp_value
                        else:
                            temp_value = temp_arr_left[y] * temp_value

                elif len(temp_arr_right) > len(temp_arr_left):
                    for y in range(0, len(temp_arr_right)):
                        if y <= len(temp_arr_left) - 1:
                            temp_value = temp_arr_right[y] * temp_arr_left[y] * temp_value
                        else:
                            temp_value = temp_arr_right[y] * temp_value

                output_list.append(temp_value)
                temp_value = 1

        return output_list


test = Solution()
print(test.productExceptSelf(arr))

# Approach 2