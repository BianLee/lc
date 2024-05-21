# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            maxVal = max(maxVal, root.val)
            if root.val >= maxVal:
                return 1 + dfs(root.left, maxVal) + dfs(root.right, maxVal)
            else:
                return dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return dfs(root, root.val)


# Another solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            count=0
            if not root:
                return 0
            if root.val >= maxVal:
                maxVal=root.val
                count+=1
            return dfs(root.left, maxVal) + dfs(root.right, maxVal) + count
        return dfs(root, root.val)
