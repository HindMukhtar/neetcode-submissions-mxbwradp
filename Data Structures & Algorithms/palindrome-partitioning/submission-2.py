class Solution:
    def isPalindrome(self,s, l, r): 

        while l < r: 
            if s[l] != s[r]: 
                return False 
            l+=1 
            r-=1 
        return True 

    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(start):

            if start == len(s): 
                res.append(subset.copy())
                return

            for end in range(start+1, len(s)+1): 
                if self.isPalindrome(s, start, end-1): 
                    subset.append(s[start:end])
                    dfs(end)
                    subset.pop()
        
        dfs(0)
        return res 


        