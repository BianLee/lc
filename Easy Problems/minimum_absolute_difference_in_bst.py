# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prevVal = float('inf')
        self.minVal = float('inf')
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.minVal = min(self.minVal, abs(self.prevVal - node.val))
            print(abs(self.prevVal - node.val))
            self.prevVal = node.val
            dfs(node.right)
            
        dfs(root)
        return self.minVal
        
