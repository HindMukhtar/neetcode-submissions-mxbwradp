class union_find: 
    def __init__(self, n): 
        self.parents = list(range(n))
        self.rank = [0]*n 

    def find(self, x): 
        if self.parents[x] != x: 
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, a, b): 

        ra = self.find(a)
        rb = self.find(b)

        if ra == rb: 
            return False 

        if self.rank[ra] > self.rank[rb]: 
            self.parents[rb] = ra
        elif self.rank[rb] > self.rank[ra]: 
            self.parents[ra] = rb
        else: 
            self.parents[rb] = ra
            self.rank[ra] += 1 

        return True 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = union_find(len(accounts))
        
        email_to_account = {}

        for account_idx, account in enumerate(accounts): 
            for email in account[1:]: 
                if email in email_to_account:
                    previous_index = email_to_account[email]
                    uf.union(account_idx, previous_index)
                else: 
                    email_to_account[email] = account_idx 

        email_by_root = defaultdict(list)

        for email, account_idx in email_to_account.items(): 
            root = uf.find(account_idx)
            email_by_root[root].append(email)

        results = []

        for root, emails in email_by_root.items(): 
            name = accounts[root][0]
            results.append([name] + sorted(emails))

        return results



        
