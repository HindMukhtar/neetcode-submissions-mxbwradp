class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        seen = set()

        queue = deque([(beginWord, 0)])

        while queue: 
            word, count = queue.popleft()
            if word in seen: 
                continue 
            if word == endWord: 
                return count+1  
            seen.add(word)

            for i, ch1 in enumerate(word): 
                for ch2 in "abcdefghijklmnopqrstuvwxyz": 
                    new_word = word[:i] + ch2 + word[i+1:]
                    if new_word in wordList: 
                        queue.append((new_word, count+1))

        return 0 