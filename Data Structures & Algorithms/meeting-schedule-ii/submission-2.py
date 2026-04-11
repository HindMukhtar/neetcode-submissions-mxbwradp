"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals: 
            return 0 

        intervals.sort(key=lambda x:x.start)

        end_times = [intervals[0].end]
        heapq.heapify(end_times)

        for i in range(1, len(intervals)): 
            start = intervals[i].start 
            end = intervals[i].end 

            if start < end_times[0]: 
                heapq.heappush(end_times, end)
            else: 
                heapq.heappop(end_times)
                heapq.heappush(end_times, end)

        return len(end_times)
        