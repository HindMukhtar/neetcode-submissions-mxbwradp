class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
