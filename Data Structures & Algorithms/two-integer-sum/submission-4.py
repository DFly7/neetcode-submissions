class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        hashmap[nums[0]] = 0

        for i in range(1, len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[nums[i]] = i

        return [0,0]

