# Solution Class
class Solution:
    def twoSum(self, nums, target):
        """
        Input type 'nums': List[int]
        Input type 'target': int
        Return type: List[int]
        """
        # Temporary dictionary to store compliment and key values
        temp_dict = {}

        # Loop through list to find target, compliment and value pairs
        for x in range(0, len(nums)):
            compliment = target - nums[x]

            # If compliment is not in the dictionary, add value to the dictionary
            if compliment not in temp_dict.keys():
                temp_dict[nums[x]] = x

            # if compliment in dictionary, return value in form of a list
            elif compliment in temp_dict.keys():
                return [temp_dict[compliment], x]


# Sample array to test solution
arr = [2, 7, 11, 15]

# Initialize solution class
test = Solution()
# Print returned value
print(test.twoSum(arr, 18))

# Source: https://leetcode.com/problems/two-sum/submissions/