'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, ans = 0, len(nums) - 1, 0
        while i < j:
            res = nums[i] + nums[j]
            if res == k:
                i += 1
                j -= 1
                ans += 1
            elif res < k:
                i+=1
            else:
                j-=1
        return ans
