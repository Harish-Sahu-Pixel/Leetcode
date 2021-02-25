'''
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order,

then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
'''


class Solution:
    def findUnsortedSubarray(self, nums):
        ans = [x == y for x, y in zip(nums, sorted(nums))]
        if all(ans):
            return 0
        else:
            return len(nums) - ans.index(False) - ans[ : : - 1].index(False)                
                        
