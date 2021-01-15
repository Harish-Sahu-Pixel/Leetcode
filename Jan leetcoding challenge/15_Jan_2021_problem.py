'''
You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums.
'''

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums, i = [0] * (n + 1), 1
        if n >= 1:
            nums[1] = 1
        while i <= n // 2:
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
            i += 1
        return max(nums)
