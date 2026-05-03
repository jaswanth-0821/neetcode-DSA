class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hash_ = defaultdict(int)
        
        for i in hand:
            hash_[i] +=1
        for num in hand:
            start = num
            while hash_[start-1]:
                start -=1
            while start<=num:
                while hash_[start]:
                    for j in range(start , start + groupSize):
                        if not hash_[j]:
                            return False
                        hash_[j] -=1
                start +=1
        return True

