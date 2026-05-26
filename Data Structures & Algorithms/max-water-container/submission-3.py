class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        maxVol = 0
        print('s')
        # Use two pointers to traverse the array in O(n) 
        while left < right:
            smallerHeight = heights[left] if heights[left] < heights[right] else heights[right]
            width = right - left 
            curVol = smallerHeight * width
            print(f'Cur Vol = {curVol}, width = {width}, height = {smallerHeight}')
            if curVol > maxVol:
                maxVol = curVol
            if heights[left] < heights[right]:
                left += 1
                continue
            if heights[right] <= heights[left]:
                right -= 1
                continue
        return maxVol