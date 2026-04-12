class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry_over = 1 
        for i in range(n-1, -1, -1): 
            if digits[i] < 9: 
                digits[i] = digits[i]+1 
                return digits
            else: 
                total = (digits[i]+carry_over)
                digits[i] = total%10 
                carry_over = total//10 

        return [carry_over] + digits 