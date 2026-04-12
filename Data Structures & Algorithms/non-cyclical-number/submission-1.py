class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set() 
        num = n

        while True: 
            digit_sum = 0 
            for digit in str(num): 
                digit_sum += int(digit)**2
            if digit_sum == 1: 
                return True  
            if digit_sum in seen: 
                return False 
            num = digit_sum
            seen.add(digit_sum)

   