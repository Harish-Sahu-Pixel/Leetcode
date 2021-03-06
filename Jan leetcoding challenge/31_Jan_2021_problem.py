'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def find_swap(nums):
            start = len(nums) - 2
            for i in range(start, -1, -1):
                flag, mini = 0, float('inf')
                for j in range(i + 1, start + 2):
                    if nums[j] > nums[i] and nums[j] <= mini:
                        flag = 1
                        mini, loc = nums[j], j
                if flag:
                    return i, loc
            return -1, -1
        i, j = find_swap(nums)
        
        if i == j == -1:
            nums.sort()
        else:
            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = nums[-1:i:-1]
