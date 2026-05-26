class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            small = numbers[left]
            big = numbers[right]

            current = big + small

            if current > target:
                right -= 1
                continue
            if current < target:
                left += 1 
                continue
            if current == target:
                return [left+1, right+1]
        return []