class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr = 1
        direction = 1
        for i in range(time):
            print(curr)
            if curr == n or (direction == -1 and curr == 1):
                direction *= -1
            curr += direction
        return curr
