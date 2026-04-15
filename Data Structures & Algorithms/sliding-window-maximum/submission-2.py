class Solution:
    def dq(): 
        dq = deque() 
        res = []
        for i, num in enumerate(nums): 

            while dq and dq[0] <= i-k: 
                # remove the first elemenr we inserted to maintain window length
                dq.popleft()

            while dq and nums[dq[-1]] <=num: 
                # if last value in queue is less than current value, remove it 
                dq.pop() 

            # add current index 
            dq.append(i)

            # append max for current window 
            if i >= k-1: 
                # last element in the queue will always be the highest for the window
                res.append(nums[dq[0]])

        return res 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        left = 0 

        for i, num in enumerate(nums): 
            heapq.heappush(heap, (-num, i))

            if i-left+1 == k: 
                while heap[0][1] < i-k+1: 
                    heapq.heappop(heap)
                res.append(-heap[0][0])
                left+=1 

        return res 

