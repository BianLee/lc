# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            arr.append(root.val)
        
        dfs(root1)
        dfs(root2)
        arr.sort()
        return arr
