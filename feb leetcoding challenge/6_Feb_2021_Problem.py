'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q1, q2 = deque(), deque()
        if root is None:
            return
        ans = [root.val]
        q1.append(root)
        while q1:
            while q1:
                if q1[0].left is not None:
                    q2.append(q1[0].left)
                if q1[0].right is not None:
                    q2.append(q1[0].right)
                q1.popleft()
            q1 = q2
            if q1:
                ans.append(q1[-1].val)
            q2 = deque()
        return ans
         
