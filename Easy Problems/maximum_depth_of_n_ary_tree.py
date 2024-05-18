"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(node):
            if not node:
                return 0
            arr = []
            for i in range(len(node.children)):
                arr.append(1 + dfs(node.children[i]))
            if len(arr)==0:
                return 0
            return max(arr)
        
        return 1+dfs(root)
