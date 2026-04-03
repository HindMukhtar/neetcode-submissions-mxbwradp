class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i = 0 
        j = n-1
        while i < j: 
            while not s[i].isalnum() and i < j: 
                i+=1 
            while not s[j].isalnum() and j > i: 
                j-=1 
            if s[i] != s[j]: 
                return False 
            i+=1 
            j-=1 
        return True 