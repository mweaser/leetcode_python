class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maximumArea = 0
        l = 0
        r = len(height) - 1
        
        while (l < r):
            currentArea = min(height[l], height[r]) * (r - l)
            maximumArea = max(maximumArea, currentArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maximumArea
            
        