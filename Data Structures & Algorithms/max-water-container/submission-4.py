class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        maxVol = 0
        # Use two pointers to traverse the array in O(n) 
        while left < right:
            smallerHeight = heights[left] if heights[left] < heights[right] else heights[right]
            curVol = smallerHeight * (right - left)
            if curVol > maxVol:
                maxVol = curVol
            if heights[left] < heights[right]:
                left += 1
                continue
            if heights[right] <= heights[left]:
                right -= 1
                continue
        return maxVol