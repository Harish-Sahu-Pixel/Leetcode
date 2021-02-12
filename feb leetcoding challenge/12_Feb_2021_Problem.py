'''
Given a non-negative integer num, return the number of steps to reduce it to zero.

If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        if num & 1:
            return 1 + self.numberOfSteps(num - 1)
        return 1 + self.numberOfSteps(num // 2)
