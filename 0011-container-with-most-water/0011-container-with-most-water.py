class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            
            curr_area = min(height[l], height[r]) * (r - l)
            print(curr_area)
            max_area = max(max_area, curr_area)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
        