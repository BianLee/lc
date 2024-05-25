# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums):
            if not nums:
                return
            root=TreeNode(max(nums))
            for i in range(len(nums)):
                if nums[i] == max(nums):
                    leftSub = nums[0:i]
                    rightSub = nums[i+1:len(nums)]
            
            root.left = build(leftSub)
            root.right = build(rightSub)
            return root
        
        return build(nums)
