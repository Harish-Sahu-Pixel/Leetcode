'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def findAverage(List):
            return sum(List) / len(List)
        q1, q2 = deque(), deque()
        ans = []
        if root is None:
            return
        q1.append(root)
        while q1:
            ans.append(findAverage([x.val for x in q1]))
            while q1:
                if q1[0].left is not None:
                    q2.append(q1[0].left)
                if q1[0].right is not None:
                    q2.append(q1[0].right)
                q1.popleft()
            q1 = q2
            q2 = deque()
        return ans
        
