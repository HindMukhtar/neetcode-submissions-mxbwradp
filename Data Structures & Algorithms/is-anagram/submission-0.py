class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}

        for letter in s: 
            s_counter[letter] = s_counter.get(letter, 0) + 1 
        
        for letter in t: 
            t_counter[letter] = t_counter.get(letter, 0) + 1 
        
        if s_counter == t_counter: 
            return True
        else: 
            return False