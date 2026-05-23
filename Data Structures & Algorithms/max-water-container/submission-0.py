class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        # difference of index of bars * the smaller height of the two
        
        area = 0


        while l < r:
            newArea = min(heights[l], heights[r]) * (r - l)

            if newArea > area:
                area = newArea
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area
                    
    



                
        