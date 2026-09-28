class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)

        if '0000' in dead: 
            return -1 

        if target == '0000': 
            return 0 

        queue = deque(["0000"])
        visited = {"0000"}
        turns = 0 

        while queue: 
            for _ in range(len(queue)): 
                state = queue.popleft()

                for i in range(4): 
                    current_digit = int(state[i])

                    for direction in [1, -1]: 
                        nxt_digit = (current_digit + direction)%10
                        nxt_state = state[:i] + str(nxt_digit) + state[i+1:] 

                        if nxt_state in dead or nxt_state in visited: 
                            continue 

                        if nxt_state == target: 
                            return turns + 1 

                        visited.add(nxt_state)
                        queue.append(nxt_state)

            turns += 1 

        return -1 