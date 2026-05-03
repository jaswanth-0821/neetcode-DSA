class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hash_ = defaultdict(int)
        
        for i in hand:
            hash_[i] +=1
        print(hash_)
        for i in hand:
            if hash_[i]:
                for j in range(i , i+groupSize):
                    if not hash_[j]:
                        return False
                    hash_[j]-=1
        return True