class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # <- -> 
        # -> -> 
        # <- <-
        # -> <- 
        # [2,4,-4,-1] process from left to right 
        
        stack = []

        for a in asteroids: 

            alive = True 

            while stack and stack[-1] > 0 and a < 0: 

                if stack[-1] < -a: 
                    stack.pop() 
                    continue 
                elif stack[-1] == -a: 
                    stack.pop() 

                alive = False 
                break  

            if alive: 
                stack.append(a)

        return stack 

