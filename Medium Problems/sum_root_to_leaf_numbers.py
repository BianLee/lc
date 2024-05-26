# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        arr=list()
        def dfs(node, s):
            if not node:
                return
            if not node.left and not node.right:
                s+=str(node.val)
                arr.append(s)
            s+=str(node.val)
            dfs(node.left, s)
            dfs(node.right, s)
        dfs(root, "")
        ans=0
        for i in range(len(arr)):
            ans+=int(arr[i])
        return ans
