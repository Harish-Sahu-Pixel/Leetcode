'''
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet,

so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values.

For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.
'''

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        while n > 0:
            x = k - 26 * (n - 1)
            if x <= 0:
                k -= 1
                ans.append('a')
            else:
                k -= x
                ans.append(chr(ord('a') + x - 1))
            n -= 1
        return ''.join(ans)
