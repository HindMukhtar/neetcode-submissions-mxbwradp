class Solution:

    def multiply(self, num1: str, num2: str) -> str:

        if len(num1) < len(num2): 
            num1, num2 = num2, num1 

        res = [0]*(len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1): 
            for j in range(len(num2)-1, -1, -1): 
                prod = int(num1[i])*int(num2[j])
                total = prod + res[i+j+1]
                res[i+j+1] = total%10
                res[i+j] += total//10 
        
        result = ''.join(map(str, res)).lstrip('0')

        return result if result else "0"
    