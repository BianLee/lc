class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        # Stack to store nodes for pre-order traversal
        # stack = [root]
        stack = [root]


        prev = None
        
        while stack:
            # Pop the current node from the stack
            current = stack.pop()
            
            # If there is a previous node, adjust its right pointer
            if prev:
                prev.right = current
                prev.left = None
            
            # Push right and left children of the current node to the stack
            # Push right first so that left is processed first in the next iteration
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            # Update the previous node to the current node
            prev = current
