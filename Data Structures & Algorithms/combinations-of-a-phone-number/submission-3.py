class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone_dict = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }
        res = []
        path = []

        def dfs(idx): 

            if len(path) == len(digits): 
                res.append("".join(path))
                return

            for letter in phone_dict[digits[idx]]:
                path.append(letter) 
                dfs(idx+1)
                path.pop()

        if digits: 
            dfs(0)

        return res