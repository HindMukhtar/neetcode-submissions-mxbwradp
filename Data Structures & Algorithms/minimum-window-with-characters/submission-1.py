class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        freq_t = {}
        for ch in t: 
            freq_t[ch] = freq_t.get(ch, 0) + 1 

        freq_s = {}
        j = 0 
        best_len = float('inf')
        best = (0,0)
        formed = 0 
        required = len(freq_t)
        for i,ch in enumerate(s):

            if ch in freq_t: 
                freq_s[ch] = freq_s.get(ch, 0) + 1 
                if freq_s[ch] == freq_t[ch]: 
                    formed +=1 

            while formed == required:
                if i - j + 1 < best_len:
                    best_len = i - j + 1
                    best = (j, i)

                left = s[j]
                if left in freq_t:
                    freq_s[left] -= 1
                    if freq_s[left] < freq_t[left]:
                        formed -= 1
                j += 1

        return "" if best_len == float('inf') else s[best[0]:best[1]+1]
            
