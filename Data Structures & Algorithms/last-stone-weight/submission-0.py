class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        MaxHeap = []
        heapq.heapify(MaxHeap)
        for n in stones:
            heapq.heappush(MaxHeap, -n)

        while len(MaxHeap) > 1:
            big = -heapq.heappop(MaxHeap)
            sec = -heapq.heappop(MaxHeap)

            if big == sec:
                continue
            
            big = big - sec

            heapq.heappush(MaxHeap, -big)
        
        if not MaxHeap:
            return 0
        return -MaxHeap[0]
