# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        maxSum=float("-inf")
        maxLevelValue=0
        level=0
        while q:
            levelSum=0
            for i in range(len(q)):
                node=q.popleft()
                levelSum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print(levelSum)
            level+=1
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevelValue = level
        return maxLevelValue
