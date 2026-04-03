class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        position, speed = zip(*pairs)
        n = len(position)
        stack = []

        for i in range(n-1, -1, -1): 
            time = (target - position[i])/speed[i]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

