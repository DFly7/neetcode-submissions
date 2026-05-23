from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        MinHeap = []
        heapq.heapify(MinHeap)

        for x1, y1 in points:
            dist = sqrt((x1)**2 + (y1)**2)
            heapq.heappush(MinHeap, (dist, x1, y1))
        
        i = 0
        res = []
        while i < k:
            minD, x, y = heapq.heappop(MinHeap)
            res.append([x, y])
            
            i += 1
        
        return res

