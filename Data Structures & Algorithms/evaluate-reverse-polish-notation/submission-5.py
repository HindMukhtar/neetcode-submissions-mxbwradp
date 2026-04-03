class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for ch in tokens: 

            if ch not in "-+*/": 
                stack.append(int(ch))

            else:
                a = stack.pop() 
                b = stack.pop() 
                if ch == '+': 
                    stack.append(a+b) 
                if ch == '*':
                    stack.append(a*b)
                if ch == '/': 
                    stack.append(int(b/a))
                if ch == '-':
                    stack.append(b-a)
        
        return stack.pop()