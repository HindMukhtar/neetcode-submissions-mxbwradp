class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        res = []
        path = []

        def dfs(start, total): 

            if total == target: 
                res.append(path.copy())
                return 

            for i in range(start, len(candidates)):  
                if total + candidates[i] > target: 
                    break 

                if i > start and candidates[i] == candidates[i-1]: 
                    continue

                path.append(candidates[i])
                dfs(i+1, total+candidates[i])
                path.pop()

        dfs(0,0)

        return res
