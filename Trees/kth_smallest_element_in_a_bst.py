# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.val == "null":
                        continue
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        res.sort()
        return res[k-1]