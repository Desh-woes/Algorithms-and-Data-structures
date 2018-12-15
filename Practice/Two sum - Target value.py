# Approach 1
def two_sum(nums, target):
    for x in range (0, len(nums)):
        for y in range (0, len(nums)):
            if x != y and nums[x] + nums[y] == target:
                return [x, y]


# Approach 2
def twosums(nums, target):
    seen_numbers = set()

    for x in nums:
        compliment = target - x
        if compliment in seen_numbers:
            return x, nums.index(compliment)
        else:
            seen_numbers.add(x)


