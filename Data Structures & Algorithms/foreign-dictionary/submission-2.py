class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = defaultdict(set)
        indeg = {c:0 for word in words for c in word}

        #generate adj and indegree list 
        for i in range(len(words)-1): 
            w1, w2= words[i], words[i+1]

            # invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))): 
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]: 
                        adj[w1[j]].add(w2[j])
                        indeg[w2[j]] += 1 
                    break

        queue = deque(k for k in indeg if indeg[k] == 0)

        output = []

        while queue: 
            letter = queue.popleft() 
            output.append(letter)

            for nei in adj[letter]: 
                indeg[nei] -= 1 
                if indeg[nei] == 0: 
                    queue.append(nei)

        return "".join(output) if len(output) == len(indeg) else ""

        