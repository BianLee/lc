class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque: always decreasing
        # deque stores the index rather than the value
        # which enables us to to tell when the bototm of the deque is outside the window
        output = []
        q = deque()
        l, r = 0, 0
        while r<len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]: #if the leftmost value in the q is out of bounds of l
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
        
            
