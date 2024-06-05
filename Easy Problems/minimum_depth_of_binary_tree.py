# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        def dfs(node, count):

            if not node.left and not node.right:
                self.ans = min(self.ans, count)
                return self.ans
            if node.left:
                dfs(node.left, count+1)
            if node.right:
                dfs(node.right, count+1)
            return self.ans
        
        if not root:
            return 0
        return dfs(root, 0)+1
