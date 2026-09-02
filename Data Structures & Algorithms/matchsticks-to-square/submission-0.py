class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        total = sum(matchsticks)
        side_length = total//4 

        if total % 4 != 0: 
            return False 

        if max(matchsticks) > side_length: 
            return False 

        matchsticks.sort(reverse=True)
        sides = [0]*4
        
        def backtrack(idx): 

            if idx == len(matchsticks): 
                return True 

            for i in range(4): 

                if sides[i] + matchsticks[idx] <= side_length: 
                    sides[i] += matchsticks[idx]

                    if backtrack(idx + 1): 
                        return True 

                    sides[i] -= matchsticks[idx]

            return False 

        return backtrack(0)
        

