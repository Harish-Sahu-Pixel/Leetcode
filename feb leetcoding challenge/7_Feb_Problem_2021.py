'''
Given a string s and a character c that occurs in s,

return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.
'''

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        dp = [0 if char == c else n for char in s]
        for i in range(1, n):
            dp[i] = min(dp[i], dp[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            dp[i] = min(dp[i], dp[i + 1] + 1)
        return dp
