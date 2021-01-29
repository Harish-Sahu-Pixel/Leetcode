'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right.

Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest.

If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = {}
        def inorder(node, x, y):
            if node is None:
                return
            inorder(node.left, x - 1, y - 1)
            if x not in d:
                d[x] = {}
            if y not in d[x]:
                d[x][y] = []
            d[x][y].append(node.val)    
            inorder(node.right, x + 1, y - 1)
        inorder(root, 0, 0)
        for x in d:
            for y in d[x]:
                d[x][y].sort()
        ans = []
        xkeys = sorted(list(d.keys()))
        for x in xkeys:
            ykeys = sorted(list(d[x].keys()), reverse = True)
            temp = []
            for y in ykeys:
                temp += d[x][y]
            ans.append(temp)
        return ans
        
