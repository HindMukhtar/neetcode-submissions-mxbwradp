class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        sol = []
        path = []

        def backtrack(i): 

            if i == len(s): 
                sol.append(' '.join(path))
                return 

            for j in range(i, len(s)): 

                if s[i:j+1] in wordSet: 
                    path.append(s[i:j+1])
                    backtrack(j+1)
                    path.pop()

        backtrack(0)

        return sol 