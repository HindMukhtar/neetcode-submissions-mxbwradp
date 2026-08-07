class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # tasks[i] = [enqueueTimei, processingTimei]

        for i, t in enumerate(tasks): 
            t.append(i)
        
        # tasks[i] = [enqueueTimei, processingTimei, i]

        tasks.sort(key = lambda t:t[0])

        res = []
        heap = []
        i = 0 
        time = tasks[0][0]

        while heap or i < len(tasks):
            # add all available tasks 
            while i < len(tasks) and tasks[i][0] <= time: 
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1 

            if not heap: 
                time = tasks[i][0]

            else: 
                proc_time, idx = heapq.heappop(heap)
                time += proc_time 
                res.append(idx)

        return res 

             
        