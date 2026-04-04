class Solution:
    def climbStairs(self, n: int) -> int:

        visited = {}
        actions = [1,2]
        ways = 0 

        def dfs(state): 
            nonlocal ways 

            if state in visited: 
                ways+=visited[state]
                return 

            if state > n: 
                return 

            if state == n: 
                ways+=1 
                return 

            for a in actions: 
                nxt_state = state+a 
                dfs(nxt_state)

            visited[state] = ways

        dfs(0)

        return ways 


        