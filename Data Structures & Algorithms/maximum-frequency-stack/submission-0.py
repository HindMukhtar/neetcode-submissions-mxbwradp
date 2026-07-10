class FreqStack:

    def __init__(self):
        self.curr_freq = {}
        self.freq_groups = defaultdict(list)
        self.max_freq = 0 

    def push(self, val: int) -> None:
        self.curr_freq[val] = self.curr_freq.get(val, 0) + 1 
        self.freq_groups[self.curr_freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.curr_freq[val])

    def pop(self) -> int:

        ans = self.freq_groups[self.max_freq].pop()
        self.curr_freq[ans] -= 1 

        if not self.freq_groups[self.max_freq]: 
            del self.freq_groups[self.max_freq]
            self.max_freq -= 1 
        return ans 



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()