# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.currNode = root
        self.counter = 0
        self.ans = []


    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.ans.append(node.val)
        self.dfs(node.right)



    def next(self) -> int:
        if self.counter == 0: 
            self.dfs(self.currNode)
            self.counter+=1
        
        self.counter+=1
        return self.ans[self.counter-2]

            
    def hasNext(self) -> bool:
        if self.counter == 0:
            self.dfs(self.currNode)
            self.counter+=1

        #print(self.ans)
        #print(self.counter)
        if self.counter-1 == len(self.ans):
            #print(self.counter)
            return False
        
        return True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
