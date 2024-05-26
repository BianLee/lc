# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        currSum = 0
        arr=list()
        def dfs(node, currSum):
            if not node:
                return
            if not node.left and not node.right:
                currSum+=node.val
                print(currSum)
                if currSum==targetSum:
                    arr.append(True)
                else:
                    arr.append(False)
                return
            currSum+=node.val
            dfs(node.left, currSum)
            dfs(node.right, currSum)

        dfs(root, 0)
        print(arr)
        if True in arr:
            return True
        return False
