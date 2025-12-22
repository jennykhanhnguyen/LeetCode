from collections import defaultdict

class DSU:
    def __init__(self):
        # parent[email] = the "representative" email of its group
        self.parent = {}

        # rank[email] = a small number that helps keep the tree shallow
        # (shallow tree => faster find)
        self.rank = {}

    def add(self, x: str) -> None:
        # If x is new, initialize it as its own parent (a new group)
        if x not in self.parent:
            self.parent[x] = x           # parent of itself => root of its own set
            self.rank[x] = 0             # start rank at 0

    def find(self, x: str) -> str:
        # Find the root (leader) of x's group
        if self.parent[x] != x:
            # Path compression:
            # rewrite parent[x] to point directly to the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]            # return the root

    def union(self, a: str, b: str) -> None:
        # Merge the groups that contain a and b
        ra = self.find(a)                # root of a
        rb = self.find(b)                # root of b

        # If same root, already in same group, nothing to do
        if ra == rb:
            return

        # Union by rank:
        # attach the smaller-rank tree under the bigger-rank tree
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb         # ra group attaches under rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra         # rb group attaches under ra
        else:
            # same rank: pick one to be parent, then increase its rank
            self.parent[rb] = ra         # rb attaches under ra
            self.rank[ra] += 1           # ra tree got taller by 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()                       # create DSU structure
        email_to_name = {}                # map each email -> its owner's name

        # 1) Build DSU connections
        for acc in accounts:              # each account like: [name, e1, e2, e3...]
            name = acc[0]                 # person's name
            first_email = acc[1]          # use the first email as the "anchor" for this account

            dsu.add(first_email)          # make sure first_email exists in DSU
            email_to_name[first_email] = name  # remember name for this email

            # connect every other email in this account with first_email
            for i in range(2, len(acc)):  # start from the second email (index 2)
                email = acc[i]            # current email

                dsu.add(email)            # ensure email exists in DSU
                email_to_name[email] = name  # map email to the name (same person)

                # union: put email and first_email in the same connected component
                dsu.union(first_email, email)

        # 2) Group emails by their DSU root
        groups = defaultdict(list)        # root_email -> list of emails in that group

        for email in email_to_name:       # iterate over all emails we have seen
            root = dsu.find(email)        # find the representative root
            groups[root].append(email)    # put this email into that root's bucket

        # 3) Build final merged answer
        result = []                       # will store merged accounts

        for root, emails in groups.items():
            emails.sort()                 # required: emails sorted lexicographically
            name = email_to_name[root]    # use root's email to get the person's name
            result.append([name] + emails)  # merged account format: [name, sorted_emails...]

        return result
