"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        pPath = []
        qPath = []
        while p:
            pPath.append(p)
            p = p.parent
        while q:
            qPath.append(q)
            q = q.parent

        for i in range(len(pPath)):
            for j in range(len(qPath)):
                if pPath[i] == qPath[j]:
                    return pPath[i]

        # print(pPath, qPath)
        

            
        
        
