class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}

        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = i
            checkMap = target - nums[i]

            if checkMap in numMap:
                if numMap[checkMap] == i:
                    continue
                return [numMap[checkMap], i]

        return []


        