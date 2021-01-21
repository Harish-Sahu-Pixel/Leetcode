'''
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) 

if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. 

For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.
'''

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i, num in enumerate(nums):
            while s and s[-1] > num and len(s) + len(nums) - i - 1 >= k:
                s.pop()
            if len(s) < k:
                s.append(num)
        return s
