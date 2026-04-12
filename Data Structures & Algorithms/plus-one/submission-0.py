class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(n) for n in digits]
        return [n for n in str(int(''.join(digits)) + 1 )]

        