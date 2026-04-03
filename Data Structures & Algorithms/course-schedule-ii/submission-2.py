class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [i for i in range(numCourses)]
        adj = defaultdict(list)
        indegree = [0]*numCourses 

        for course, prereq in prerequisites: 
            adj[prereq].append(course)
            indegree[course]+=1 

        queue = deque() 

        for course, ind in enumerate(indegree):
            if ind == 0: 
                queue.append(course)

        output = []

        while queue: 
            node = queue.popleft() 
            output.append(node)
            for nei in adj[node]: 
                indegree[nei] -= 1 
                if indegree[nei] == 0: 
                    queue.append(nei)

        return output if len(output) == numCourses else []



