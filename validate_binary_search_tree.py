# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        for i in range(len(self.arr)):
            if i+1<len(self.arr):
                if self.arr[i] < self.arr[i+1]:
                    continue
                else:
                    return False

        return True
