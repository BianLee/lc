# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        arr = list()
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        
        self.i=0
        def secondDfs(root):
            if not root:
                return 
            secondDfs(root.left)
            root.val = sum(arr[self.i:])
            self.i+=1
            secondDfs(root.right)

        dfs(root)
        secondDfs(root)
        return root
