'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];
        for character in s:
            if character=='(' or character=='{' or character=='[':
                stack.append(character)
            else:
                if len(stack)>0:
                    if character==')' and stack[-1]=='(':
                        stack.pop()
                    elif(character=='}' and stack[-1]=='{'):
                        stack.pop()
                    elif(character==']' and stack[-1]=='['):
                        stack.pop()   
                    else:
                        return False
                else:
                    return False
        else:
            if len(stack)>0:
                return False
            else:
                return True
