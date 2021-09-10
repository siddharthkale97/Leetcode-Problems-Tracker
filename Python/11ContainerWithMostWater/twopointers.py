class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i = 0
        j = len(height)-1
        while(i<j):
            area = (j-i) * min(height[i],height[j])
            if area>maxarea:
                maxarea = area
            if height[i] <= height[j]:
                i += 1
            elif height[j] <= height[i]:
                j -= 1
        return maxarea