class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i, c in enumerate(s)}
        res = []
        length = 0 
        start = 0 
        for i, c, in enumerate(s): 
            start = max(start, last[c])
            length +=1 
            if i == start: 
                res.append(length)
                length = 0 

        return res 
        