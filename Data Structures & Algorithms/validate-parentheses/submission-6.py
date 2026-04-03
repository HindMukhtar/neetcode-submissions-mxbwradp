class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']

        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []

        for i, ch in enumerate(s): 
            if ch in pairs.values(): 
                stack.append(ch)

            else:
                if stack: 
                    op = stack.pop() 
                    if op != pairs[ch]: 
                        return False
                else: 
                    return False  

        return True if not stack else False