class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total_time = []
        new_data = []
        for p,s in zip(position, speed):
            new_data.append((p,s))
        new_data = sorted(new_data)
        for p,s in new_data:
            total_time.append((target - p)/s)

        stack = []
        for t in total_time[::-1]:
            if not stack:
                stack.append(t)
            elif stack[-1]<t:
                stack.append(t)

        return len(stack)
                