class Solution:
    def test(): 

        if len(num1) < len(num2): 
            num1, num2 = num2, num1 

        def mult(n2, n1): 
            ans = []
            carry_over = 0 
            for i in range(len(n2)-1, -1, -1): 
                prod = int(n1)*int(n2[i])+carry_over
                carry_over = prod//10 
                ans.append(str(prod%10))
            if carry_over > 0: 
                ans.append(str(carry_over))
            return ans

        res = []
        for j in range(len(num2)-1, -1, -1): 
            res = mult(num2[j], num1)
            res = [str(0)]*(len(num2)-j-1) + res
        
        return ''.join(reversed(res))

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
    