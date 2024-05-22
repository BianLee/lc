# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        total = TreeNode()
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            
            self.curr.left = None
            self.curr.right = TreeNode(node.val)
            self.curr = self.curr.right

            dfs(node.right)

        dummy = TreeNode(0)
        self.curr = dummy
        dfs(root)
        return dummy.right
