'''
Given two sequences pushed and popped with distinct values,

return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped)
