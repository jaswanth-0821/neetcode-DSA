class Solution:
    def trap(self, height: List[int]) -> int:
        left_high = [0]*len(height)
        right_high = [0]*len(height)
        left_maxi = height[0]
        for i in range(1,len(height)):
            if height[i]<left_maxi:
                left_high[i] = left_maxi
            else:
                left_maxi = height[i]

        right_maxi = height[-1]
        for i in range(len(height)-2 , 0, -1):
            if height[i]<right_maxi:
                right_high[i] = right_maxi
            else:
                right_maxi = height[i]

        
        total_liq = 0
        for i in range(len(height)):
            if left_high[i]==0 or right_high[i]==0:
                continue
            total_liq += (min(left_high[i],right_high[i])-height[i])

        return total_liq
