class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        j = 0 
        longest = 0 
        maxfreq = 0 
        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1 
            maxfreq = max(maxfreq, freq[ch])
            while ((i-j+1) - maxfreq) > k: 
                freq[s[j]] -= 1
                j+=1 
            longest = max(longest, i-j+1)
        return longest 