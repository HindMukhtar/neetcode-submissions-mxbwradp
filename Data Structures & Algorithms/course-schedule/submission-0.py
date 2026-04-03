class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [i for i in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        done = [False for _ in range(numCourses)]
        adj = defaultdict(list)

        def dfs(node): 
                
            if done[node]: 
                return False 

            if visited[node]: 
                return True 

            visited[node] = True
            
            for nei in adj[node]: 
                if dfs(nei): 
                    return True
            
            visited[node] = False
            done[node] = True 

            return False 

        for course, prereq in prerequisites: 
            adj[prereq].append(course)

        for course in courses: 
            if dfs(course): 
                return False 
        
        return True 

        
