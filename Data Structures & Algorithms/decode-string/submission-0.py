class Solution:
    def decodeString(self, s: str) -> str:
        # if we see a character then append to current 
        # if we see a digit then keep tracking the digit 
        # if we see an open bracket, then move current 
        # string to stack and start over 
        # when we see close bracket then multiply current string 
        # by digit and append to previous string 

        digit = 0 
        curr = [] 
        ans = []
        stack = []

        for ch in s: 

            if ch.isdigit(): 
                digit = int(ch) + 10*digit
            
            elif ch == '[': 
                stack.append(''.join(curr))
                stack.append(digit)
                digit = 0 
                curr = []

            elif ch == ']': 
                num = stack.pop() 
                prev = stack.pop()
                combined = prev + (num*''.join(curr))
                curr = [combined]

            else: 
                curr.append(ch)

        return ''.join(curr)