'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for char in S:
            if char.isalpha():
                ans = [i + j for i in ans for j in [char.upper(), char.lower()]]
            else:
                ans = [i + char for i in ans]
        return ans
