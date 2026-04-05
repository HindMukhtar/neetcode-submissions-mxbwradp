class Solution:

    def countSubstrings(self, s: str) -> int:

        num_palindromes = 0 

        def expand(l, r): 
            nonlocal num_palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                l-=1 
                r+=1 
                num_palindromes+=1 


        for i in range(len(s)): 
            expand(i, i)
            expand(i, i+1)

        return num_palindromes

        