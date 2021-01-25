'''
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.
'''

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = {1 : []}
        for i, num in enumerate(nums):
            if num:
                counter[1].append(i)
        print(counter[1])
        for i in range(len(counter[1]) - 1):
            if counter[1][i + 1] - counter[1][i] - 1 < k:
                return False
        return True
