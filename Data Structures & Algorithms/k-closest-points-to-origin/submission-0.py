from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        MinHeap = []
        heapq.heapify(MinHeap)

        for x1, y1 in points:
            dist = sqrt((x1)**2 + (y1)**2)
            heapq.heappush(MinHeap, dist)
        
        i = 0
        res = []
        while i < k:
            maxD = heapq.heappop(MinHeap)
            for x1, y1 in points:
                dist = sqrt((x1)**2 + (y1)**2)
                if [x1,y1] in res:
                    continue
                if dist == maxD:
                    res.append([x1,y1])
                    break
            i += 1
        
        return res

