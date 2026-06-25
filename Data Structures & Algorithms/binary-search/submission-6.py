class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        mid = (r + l) // 2 

        if nums[mid] > target:
            r = mid - 1
            return self.binary_search(l, r, nums, target)
        elif nums[mid] < target:
            l = mid + 1
            return self.binary_search(l, r, nums, target)
        else:
            return mid
        
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1
        return self.binary_search(l, r, nums, target)
        