# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        #2 --> OR
        #3 --> AND
        def dfs(root):
            if not root.left and not root.right:
                if root.val == 0:
                    return False
                elif root.val == 1:
                    return True
            if (root.left and root.right) and 0 <= root.left.val <= 1 and 0 <= root.right.val <= 1:
                if root.val == 2: #OR
                    if root.left.val + root.right.val >= 1:
                        return True
                    else:
                        return False
                elif root.val == 3: #AND
                    if root.left.val + root.right.val == 2:
                        return True
                    else:
                        return False
                    
            if root.val == 2:
                leftSide = dfs(root.left)
                rightSide = dfs(root.right)
                print(leftSide)
                print(rightSide)
                return leftSide or rightSide
            elif root.val == 3:
                leftSide = dfs(root.left)
                rightSide = dfs(root.right)
                return leftSide and rightSide

        return dfs(root)
