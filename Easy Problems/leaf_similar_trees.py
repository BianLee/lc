# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans=[]
        def dfs(node):
            if node and not node.left and not node.right:
                ans.append(node.val)
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
        dfs(root1)
        resOne = ans
        ans=[]
        dfs(root2)
        resTwo = ans
        return resOne == resTwo
