class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        while l<r:
            leftMax, rightMax = heights[l], heights[r]
            water = min(leftMax,rightMax)*(r-l)
            max_water = max(max_water,water)
            if leftMax <= rightMax:
                l+=1
            if leftMax > rightMax:
                r-=1


        return max_water
