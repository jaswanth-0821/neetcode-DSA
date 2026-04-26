class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i =0
        j = len(heights)-1
        while i<j:
            curr_area = min(heights[i],heights[j])*(abs(j-i))
            if heights[i]<heights[j]:
                i = i+1
            else:
                j = j-1
            area = max(area,curr_area)

        return area
            