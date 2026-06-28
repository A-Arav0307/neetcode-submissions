from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parent = {}
        self.email_to_name = {}

        def find(x): 
            while x != self.parent[x]: 
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(n1, n2):
            root_a = find(n1)
            root_b = find(n2)

            if root_a != root_b: 
                self.parent[root_a] = root_b 

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                self.parent[email] = email
                self.email_to_name[email] = name

        groups = defaultdict(list)

        for account in accounts: 
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        for email in self.parent:
            root = find(email)
            groups[root].append(email)

        res = []

        for root, emails in groups.items():
            name = self.email_to_name[root]
            res.append([name] + sorted(emails))

        return res

        