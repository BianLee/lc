# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.temp = list()
        self.ans = []
        self.backtracking = False
        def dfs(node):
            if not node:
                return
            
            self.temp.append(node.val)
            self.backtracking = False
            

            dfs(node.left)
            dfs(node.right)
            if not self.backtracking:
                self.ans.append(tuple(self.temp))
            self.backtracking = True
            self.temp = self.temp[:len(self.temp)-1]
            

        dfs(root)
        #print(self.ans)

        final = []
        for i in range(len(self.ans)):
            build = ""
            for n in self.ans[i]:
                
                build+=str(n)+"->"
            build = build[:len(build)-2]
            final.append(build)
        return final
