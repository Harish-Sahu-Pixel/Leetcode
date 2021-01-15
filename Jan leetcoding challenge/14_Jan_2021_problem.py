'''
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ref = sum(nums) - x
        if ref < 0:
            return -1
        dq, i, rec, ans = collections.deque(), 0, 0, float('-inf')
        while i < len(nums):
            dq.append(nums[i])
            rec += nums[i]
            if rec == ref:
                if len(dq) > ans:
                    ans = len(dq)  
            elif rec > ref:
                while rec > ref:
                    rec -= dq[0]
                    dq.popleft()
                if rec == ref:
                    if len(dq) > ans:
                        ans = len(dq)
            i += 1
        if ans != float('-inf'):
            return len(nums) - ans
        return -1
