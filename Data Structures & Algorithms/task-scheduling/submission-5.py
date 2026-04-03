class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # get frequency of each tasks 
        task_frequency = {}

        for t in tasks: 
            task_frequency[t] = task_frequency.get(t, 0) + 1 

        # We want to start with the most frequent task 
        # Use a heap to store the most frequent task 
        max_heap = [-v for v in task_frequency.values()]
        heapq.heapify(max_heap)
        task_queue = deque() 

        time = 0 

        while max_heap or task_queue: 
            time+=1 
            if max_heap: 
                v = heapq.heappop(max_heap)
                if -(v+1) > 0: 
                    # If we need to process this task again, store it in te queue
                    task_queue.append((v+1, time+n))

            if task_queue and time == task_queue[0][1]: 
                v,  time_check = task_queue.popleft()
                heapq.heappush(max_heap, v) 

        return time 




        
        