class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1] +=1
            return digits
        remainder = 1
        rs = []
        for i in digits[::-1]:
            print(remainder)
            if i==9 and remainder:
                rs.append(0)
                remainder = 1
            else:
                rs.append(i+remainder)
                remainder =0
        if remainder:
            rs.append(1)
        return rs[::-1]
