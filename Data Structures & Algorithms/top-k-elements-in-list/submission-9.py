class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        print(frequency)

        out = []
        count = 0
        for key, val in frequency.items():
            out.append([val, key])
        out.sort()

        res=[]
        while len(res) < k:
            res.append(out.pop()[1])
        return res


