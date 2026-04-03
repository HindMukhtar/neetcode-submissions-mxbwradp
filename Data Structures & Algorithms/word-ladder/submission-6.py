class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList: 
            return 0
        
        
        wordset = set(wordList)

        queue = deque([(beginWord, 1)])
        seen = set(beginWord)

        while queue: 
            word, count = queue.popleft()

            if word == endWord: 
                return count 

            for i, ch1 in enumerate(word): 
                for ch2 in "abcdefghijklmnopqrstuvwxyz": 
                    new_word = word[:i] + ch2 + word[i+1:]
                    if new_word in wordset and new_word not in seen: 
                        seen.add(new_word)
                        queue.append((new_word, count+1))

        return 0 