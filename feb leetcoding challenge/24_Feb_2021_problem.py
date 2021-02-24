'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1

AB has score A + B, where A and B are balanced parentheses strings.

(A) has score 2 * A, where A is a balanced parentheses string.
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0]
        for char in S:
            if char == '(':
                stack.append(0)
            else:
                temp = stack.pop()
                stack[-1] += max(2 * temp, 1)
        return stack.pop()
