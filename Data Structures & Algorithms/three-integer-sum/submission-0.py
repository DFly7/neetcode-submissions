class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # For n in nums we want to see if there are two other numbers
        # that can be added to this to == 0
        # We can do this with a sliding window approach if teh array is ordered
        nums = sorted(nums)
        out = []
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            # DUPLICATE SKIP 1: Skip if this starting number is a duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curNum = nums[i]
            while left < right:
                leNum = nums[left]
                riNum = nums[right]

                diff = curNum + leNum + riNum
                if diff < 0:
                    left += 1
                    continue
                if diff > 0:
                    right -= 1
                    continue
                if diff == 0:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # DUPLICATE SKIP 2: Skip same numbers on left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    continue
        return out

