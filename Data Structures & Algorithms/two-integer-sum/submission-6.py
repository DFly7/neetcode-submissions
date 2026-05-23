class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        
        for i, n in enumerate(nums):
            diff = target - n

            if diff in diffDict:
                return [diffDict[diff], i]
            
            diffDict[n] = i

        return []
            
