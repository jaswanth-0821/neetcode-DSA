class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for task in tasks:
            freq[ord(task) - ord("A")] +=1
        
        maxf = max(freq)
        maxc = 0
        for i in freq:
            maxc += 1 if i==maxf else 0
        
        time = (maxf -1)*(n+1) + maxc
        return max(time, len(tasks))