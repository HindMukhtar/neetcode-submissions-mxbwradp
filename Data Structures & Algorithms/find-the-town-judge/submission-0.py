class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        indegree = {i:0 for i in range(1,n+1)}
        outdegree = {i:0 for i in range(1,n+1)}

        for a, b in trust: 
            indegree[b] += 1 
            outdegree[a] += 1 

        for person in range(1, n+1): 
            if indegree[person] == n-1 and outdegree[person] == 0: 
                return person 

        return -1 

