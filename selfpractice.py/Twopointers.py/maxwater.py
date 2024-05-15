class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the current area
            current_water = min(height[left], height[right]) * (right - left)
            # Update max water if the current area is greater
            max_water = max(max_water, current_water)
            
            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
sol = Solution()
maxarea= [1,78,98,3,-9,78,0,9,100]
print("The maximum area is:", sol.maxArea(maxarea))