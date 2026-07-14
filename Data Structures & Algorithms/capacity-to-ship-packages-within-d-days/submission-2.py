class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        # binary search on answer. We need to define a min and max capacity 
        # for the ship weight 
        # min would be the max weight of all packages 
        # max would be the sum of all weights of all packages 
        # then we need to define a function called can ship which returns a true or false
        # function will count days needed. will add new day everytime we go over 
        # the capacity 
        # then return true if days is less than or equal to days 

        def can_ship(capacity):

            needed = 1 
            total = 0 

            for w in weights: 

                total += w 

                if total > capacity: 
                    needed += 1 
                    total = w 

            return needed <= days 

        lo = max(weights)
        hi = sum(weights)

        while lo < hi: 

            mid = (lo+hi)//2 

            if can_ship(mid): 
                hi = mid 
            else: 
                lo = mid + 1 

        return lo 