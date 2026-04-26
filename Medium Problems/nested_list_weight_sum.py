class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        self.answer = 0

        def recursive(passed_list, depth):

            for item in passed_list:
                if item.isInteger():
                    self.answer += item.getInteger() * depth
                else:
                    recursive(item.getList(), depth+1)
            
        
        recursive(nestedList, 1)
        return self.answer
