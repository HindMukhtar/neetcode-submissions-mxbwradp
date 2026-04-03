class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            #key = ''.join(sorted(w))
            count = [0]*26 
            for c in w: 
                count[ord(c) - ord('a')] += 1 
            key = tuple(count)
            groups[key].append(w)

        return list(groups.values())