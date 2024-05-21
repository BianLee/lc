# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        def dfs(root):
            
            if not root: 
                return None
            if root == p or root == q:
                return root

            l = dfs(root.left)
            r = dfs(root.right)
            
            if l and r: #both have values
                return root
            
            return l or r #return whichever one that is not None

        return dfs(root)
