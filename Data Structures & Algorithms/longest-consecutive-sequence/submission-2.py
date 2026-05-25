class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        have = set()

        startOfSeq = set()

        for n in nums:
            have.add(n)
        
        for n in nums:
            previous = n -1 
            if previous not in have:
                startOfSeq.add(n)
        print(startOfSeq)

        highestSeq = 0
        for n in startOfSeq:
            currentSeq = 0
            num = n 
            while num in have:
                currentSeq +=1
                num += 1
            if currentSeq > highestSeq:
                highestSeq = currentSeq
        return highestSeq

