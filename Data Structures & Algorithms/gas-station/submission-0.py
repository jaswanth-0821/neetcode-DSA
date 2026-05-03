class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        new_ = []
        for a,b in zip(gas,cost):
            new_.append(a-b)
        if sum(new_)<0:
            return -1
        res = 0
        total = 0
        for i in range(len(new_)):
            total +=new_[i]
            if total<0:
                total = 0
                res = i+1
        return res
        