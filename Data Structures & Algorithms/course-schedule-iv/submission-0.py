class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses 

        for pre, course in prerequisites: 
            adj[pre].append(course)
            indeg[course] += 1 

        ancestors = [set() for _ in range(numCourses)]

        queue = deque(
            course 
            for course in range(numCourses)
            if indeg[course] == 0 
        )

        while queue: 
            pre = queue.popleft() 

            for course in adj[pre]: 
                ancestors[course].add(pre)

                ancestors[course].update(ancestors[pre])

                indeg[course] -=1 

                if indeg[course] == 0: 
                    queue.append(course)

        return [prerequisite in ancestors[course] for prerequisite, course in queries]
        
