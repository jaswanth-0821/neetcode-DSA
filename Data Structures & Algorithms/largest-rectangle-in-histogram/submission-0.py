class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            mini = heights[i]
            for j in range( i  , len(heights)):
                
                mini = min(heights[j],mini)
                area = max(mini*((j-i)+1),area)
              
        return area

