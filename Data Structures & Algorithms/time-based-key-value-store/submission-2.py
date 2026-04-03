class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.keys[key]
        lo, hi = 0, len(values) - 1 
        if values: 
            while lo < hi: 

                mid = (lo+hi)//2 

                if values[mid][0] == timestamp: 
                    return values[mid][1]
                elif values[mid][0] > timestamp: 
                    hi = mid - 1 
                else: 
                    lo = mid + 1
            
            if values[lo][0] <= timestamp: 
                return values[lo][1]
            elif values[lo-1][0] <= timestamp: 
                return values[lo-1][1]
            else: 
                return ""
        else: 
            return ""
        
