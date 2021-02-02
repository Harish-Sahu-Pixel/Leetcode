'''
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high].

Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant).

It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
            
        return trim(root)
