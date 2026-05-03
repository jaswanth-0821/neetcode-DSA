class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = triplets
        for i in range(3):
            tmp = []
            for j in res:
                if j[i] <=target[i]:
                    tmp.append(j)
            res = tmp
        if not res:
            return False
        ans = res[0]
        for i in res:
            ans = [max(i[0] , ans[0]),max(i[1] , ans[1]),max(i[2] , ans[2])]
        
        return True if ans==target else False