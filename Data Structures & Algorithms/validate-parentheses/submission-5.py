class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']

        stack = []

        for i, ch in enumerate(s): 
            if ch in open_brackets: 
                stack.append(ch)

            else:
                if stack: 
                    op = stack.pop() 
                    if (ch == ')' and op != '(') or (ch == ']' and op != '[') or (ch == '}' and op != '{') : 
                        return False
                else: 
                    return False  

        return True if not stack else False