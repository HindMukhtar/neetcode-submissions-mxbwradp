class Solution:

    def longestPalindrome(self, s: str) -> str:

        longest = 0 
        max_l = 0 
        max_r = 0

        def expand(l, r): 
            nonlocal longest, max_l, max_r

            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l) > longest: 
                    longest = (r-l)
                    max_l = l 
                    max_r = r
                l-=1 
                r+=1

        for i in range(len(s)): 
            expand(i, i)
            expand(i, i+1)

        return s[max_l:max_r+1]
