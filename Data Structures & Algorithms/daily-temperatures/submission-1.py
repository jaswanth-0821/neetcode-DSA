class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for idx in range(len(temperatures) - 1, -1, -1):
           
            

            while stack and  temperatures[stack[-1]]<=temperatures[idx]:
                stack.pop()
            
            if not stack:
                result.append(0)
                stack.append(idx)
                
            else:
                result.append((stack[-1] - idx) )
                stack.append(idx)
            print(stack)
        return result[::-1]

            

        