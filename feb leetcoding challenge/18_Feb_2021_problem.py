'''
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:
'''

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans, i = [0, 0], 1
        for j in range(2, len(A)):
            if A[j] - A[j-1] == A[j-1] - A[j-2]:
                ans.append(ans[j - 1] + i)
                i += 1
            else:
                ans.append(ans[j - 1])
                i = 1
        return ans[-1]
