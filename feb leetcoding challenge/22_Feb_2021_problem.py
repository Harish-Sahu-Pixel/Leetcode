'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string.

If there are more than one possible results, return the longest word with the smallest lexicographical order.If there is no possible result, return the empty string.
'''

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isPresent(s, t):
            i = j = 0
            while i < len(s):
                #print(i, j)
                if j >= len(t):
                    return True
                if s[i] == t[j]:
                    j += 1
                i += 1
            if j >= len(t):
                return True
            return False
                    
        d.sort()
        d.sort(key = lambda x : len(x), reverse = True)
        for i in range(len(d)):
            if isPresent(s, d[i]):
                return d[i]
        return ''
