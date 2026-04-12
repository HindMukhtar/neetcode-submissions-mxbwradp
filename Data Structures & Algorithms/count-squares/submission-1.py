class CountSquares:

    def __init__(self):
        self.ptsCount = {}
        self.points = []
        
    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        self.points.append(point)
        self.ptsCount[pt] = self.ptsCount.get(pt, 0) + 1 

    def count(self, point: List[int]) -> int:
        count = 0 
        x1, y1 = point[0], point[1]

        for (x2, y2), freq in self.ptsCount.items(): 
            if abs(x1-x2) == abs(y1-y2)  and x1 != x2: 
                # can form a square, check other corners 
                right_corner = (x1, y2)
                left_corner = (x2, y1)
                if right_corner in self.ptsCount and left_corner in self.ptsCount: 
                    count += freq*self.ptsCount[right_corner]*self.ptsCount[left_corner]
        return count 
