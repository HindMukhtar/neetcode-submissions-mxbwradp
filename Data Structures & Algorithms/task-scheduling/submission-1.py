class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # get frequency of each tasks 
        task_frequency = {}

        for t in tasks: 
            task_frequency[t] = task_frequency.get(t, 0) + 1 

        # We want to start with the most frequent task 
        # Use a heap to store the most frequent task 
        max_heap = [(-v, k) for k, v in task_frequency.items()]
        heapq.heapify(max_heap)
        task_queue = deque() 

        time = 0 

        while max_heap or task_queue: 
            if max_heap: 
                v, k = heapq.heappop(max_heap)

                if -(v+1) > 0: 
                    # If we need to process this task again, store it in te queue
                    task_queue.append((v+1, k, time+n))

            while task_queue and time >= task_queue[0][2]: 
                v, k, time_check = task_queue.popleft()
                heapq.heappush(max_heap, (v, k)) 

            time+=1 

        return time 




        
        