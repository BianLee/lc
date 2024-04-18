class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1 and flowerbed[0] == 0 and n==1:
                return True
            if flowerbed[i] == 1:
                continue
            else:
                if i == 0:
                    if i+1 < len(flowerbed) and flowerbed[i+1] == 0 and n>0:
                        flowerbed[i] = 1
                        n-=1
                elif i == len(flowerbed)-1:
                    if 0 < i-1 and flowerbed[i-1] == 0 and n>0:
                        flowerbed[i] = 1
                        n-=1
                else:
                    if i+1 < len(flowerbed) and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and n>0:
                        flowerbed[i] = 1
                        n-=1 
        if n == 0:
            return True
        else:
            return False
            