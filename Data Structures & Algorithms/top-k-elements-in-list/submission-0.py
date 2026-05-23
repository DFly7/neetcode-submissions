class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        output = []

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        i=0
        while i<k:
            number = max(hashMap, key=hashMap.get)
            del hashMap[number]
            output.append(number)
            i += 1
        
        return output


            
        