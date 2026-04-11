class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0 

        while i < len(intervals) and intervals[i][1] < newInterval[0]: 
            if merged and merged[-1][1] >= intervals[i][0]: 
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else: 
                merged.append(intervals[i])
            i += 1
        
        if merged and merged[-1][1] >= newInterval[0]: 
            merged[-1][0] = min(merged[-1][0], newInterval[0])
            merged[-1][1] = max(merged[-1][1], newInterval[1])    
        else: 
            merged.append(newInterval)         

        while i < len(intervals): 
            if merged and merged[-1][1] >= intervals[i][0]: 
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else: 
                merged.append(intervals[i])
            i += 1

        return merged 
