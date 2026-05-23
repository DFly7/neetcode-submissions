class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        MaxHeap = []
        heapq.heapify(MaxHeap)
        for n in nums:
            heapq.heappush(MaxHeap, -n)
        
        while k>0:
            out = heapq.heappop(MaxHeap)
            k-=1

        return -out