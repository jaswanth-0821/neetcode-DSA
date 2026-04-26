class Solution:
    def get_answer(self , v1,v2,operator):
        if operator=="+":
            return v2+v1
        elif operator=="-":
            return v2-v1
        elif operator=="*":
            return v2*v1
        elif operator=="/":
            return v2/v1

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token  in tokens:
            if token not in ["+", "-","*","/"]:
                stack.append(token)
                continue
            
            value1 = int(stack.pop())
            value2 = int(stack.pop())
            answer = self.get_answer(value1,value2 , token)
            stack.append(answer)
        
        return int(stack[-1])