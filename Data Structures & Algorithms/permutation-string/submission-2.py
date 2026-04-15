class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        if n < m: 
            return False 

        s1_check = [0]*26 
        for ch in s1: 
            s1_check[ord(ch) - ord('a')] += 1 

        j = 0 
        s2_check = [0]*26
        for i, ch in enumerate(s2): 
            s2_check[ord(ch) - ord('a')] += 1 

            # Shrink of window gets too big 
            if (i-j+1) > m: 
                s2_check[ord(s2[j]) - ord('a')] -=1
                j += 1 

            if s2_check == s1_check: 
                return True 
        
        return False 