class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        remaining = {}
        for c in hand: 
            remaining[c] = remaining.get(c, 0) + 1 

        while remaining: 
            start = min(remaining)
            for card in range(start, start+groupSize): 
                if card not in remaining: 
                    return False 
                remaining[card] -=1 
                if remaining[card] == 0: 
                    del remaining[card]

        return True 



        