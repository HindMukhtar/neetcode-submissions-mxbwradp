class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        ss = deque() 
        n = len(s)
        j = 0 
        for i, ch in enumerate(s): 
            while ch in ss: 
                j += 1 
                ss.popleft()
            ss.append(ch)
            longest = max(longest, len(ss))

        return longest 