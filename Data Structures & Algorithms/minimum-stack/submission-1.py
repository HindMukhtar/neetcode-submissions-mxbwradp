class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        # If it's the first element 
        if not self.stack and not self.minstack: 
            self.stack.append(val)
            self.minstack.append(val)
        elif val <= self.minstack[-1]: 
            self.stack.append(val)
            self.minstack.append(val)
        else: 
            self.stack.append(val)
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
