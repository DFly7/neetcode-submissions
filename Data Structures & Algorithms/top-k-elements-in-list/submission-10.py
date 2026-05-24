class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, val in freq.items():
            bucket[val].append(key)

        out = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                out.append(num)
            if len(out) == k:
                return out
            


            