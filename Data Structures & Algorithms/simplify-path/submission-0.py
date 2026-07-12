class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_list = path.split('/')
        ans = []

        for ch in path_list: 
            if ch == '.': 
                continue 
            elif ch == '': 
                continue 
            elif ch == '..': 
                if ans: 
                    ans.pop()
            else: 
                ans.append(ch)

        return '/' + '/'.join(ans)