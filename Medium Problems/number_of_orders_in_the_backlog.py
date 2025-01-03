class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
    
        buyHeap = []
        sellHeap = []
        heapq.heapify(buyHeap)
        heapq.heapify(sellHeap)
        buyLookup, sellLookup = defaultdict(int), defaultdict(int)

        for i in range(len(orders)):
            price, quantity, orderType = orders[i]
            counter = quantity
            if orderType == 0: #buy order
                while len(sellHeap) > 0 and sellHeap[0] <= price and counter>0:
                    matched_quantity = min(counter, sellLookup[sellHeap[0]])
                    sellLookup[sellHeap[0]] -= matched_quantity
                    counter -= matched_quantity
                    if sellLookup[sellHeap[0]] == 0:
                        heapq.heappop(sellHeap)

               
                if counter>0:
                    heapq.heappush(buyHeap, -price)
                    heapq.heapify(buyHeap)
                    buyLookup[price] += counter
            
                
                    
            elif orderType == 1:
                while len(buyHeap)>0 and -(buyHeap[0]) >= price and counter>0:
                    matched_quantity = min(counter, buyLookup[-buyHeap[0]])
                    buyLookup[-buyHeap[0]] -= matched_quantity
                    counter -= matched_quantity
                    if buyLookup[-buyHeap[0]] == 0:
                        heapq.heappop(buyHeap)

                
                if counter>0:
                    heapq.heappush(sellHeap, price)
                    heapq.heapify(sellHeap)
                    sellLookup[price] += counter
            
                

        print(buyHeap)
        print(sellHeap)
        print(buyLookup)
        print(sellLookup)
        ans = 0
        for key,value in buyLookup.items():
            if value>0:
                ans+=value
        for key,value in sellLookup.items():
            if value>0:
                ans+=value
        
        return ans % (10**9 + 7)
        
        # return 0
