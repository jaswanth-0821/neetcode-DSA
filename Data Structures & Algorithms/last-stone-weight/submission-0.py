class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mxheap = [-1*stone for stone in stones]

        heapq.heapify(mxheap)
        
        while len(mxheap)>1:
            val1 = -1* heapq.heappop(mxheap)
            val2 = -1* heapq.heappop(mxheap)

            if val1==val2:
                continue
            
            remaining = -1*abs(val1-val2)
            heapq.heappush(mxheap , remaining)
        
        if mxheap:
            return -1*mxheap[0]
        return 0