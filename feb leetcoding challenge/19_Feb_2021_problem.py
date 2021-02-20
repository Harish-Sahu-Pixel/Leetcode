'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or

It can be written as AB (A concatenated with B), where A and B are valid strings, or

It can be written as (A), where A is a valid string.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idxs, stack = set(), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((s[i], i))
            elif s[i] == ')':
                if not stack:
                    idxs.add(i)
                else:
                    stack.pop()
        while stack:
            idxs.add(stack[-1][1])
            stack.pop()
        return ''.join([s[i] for i in range(len(s)) if i not in idxs])
