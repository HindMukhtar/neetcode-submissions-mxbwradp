class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # [1,2,3]

        nums = list(i+1 for i in range(n))
        combinations = []

        def dfs(i, path): 

            if len(path) == k: 
                combinations.append(path.copy())
                return 

            for j in range(i, n): 
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()


        dfs(0, [])
        return combinations



        