# Accounts merge
"""
Given a list of accounts where each element account [i] is a list of strings,
where the first element account [i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, merge these accounts. Two accounts definitely belong to the same person if there is
some common email to both accounts.
Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in sorted order.
"""
"""
Input: N = 4,
accounts =
[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

Output: [["John","john00@mail.com","john_newyork@mail.com", "johnsmith@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

Explanation:
The first and the second John are the same person as they have a common email.
But the third Mary and fourth John are not the same as they do not have any common email.
The result can be in any order but the emails must be in sorted order. The following is also a valid result:

[['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com' , 'john_newyork@mail.com', 'johnsmith@mail.com' ]]
"""
"""
Input: N = 6,
accounts =
[["John","j1@com","j2@com","j3@com"],
["John","j4@com"],
["Raj",”r1@com”, “r2@com”],
["John","j1@com","j5@com"],
["Raj",”r2@com”, “r3@com”],
["Mary","m1@com"]]

Output:
[["John","j1@com","j2@com","j3@com","j5@com"],
["John","j4@com"],
["Raj",”r1@com”, “r2@com”, “r3@com”],
["Mary","m1@com"]]

Explaination:
The first and the fourth John are the same
person here as they have a common email.
And the third and the fifth Raj are also the same person.
So, the same accounts are merged.
"""
"""
Constraints:
- 1 <= N <= 1000
- 2 <= accounts[i].size <= 15
- 1 <= accounts[i][j].size <= 30
- accounts[i][0] consists of English letters.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parent = [j for j in range(V)]
        self.sizes = [1 for _ in range(V)]

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])

        return self.parent[node]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution:
    def accountsMerge(self, accounts):
        """
        [["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]]
        """
        mail_to_ind = {}
        ds = DisjointSet(len(accounts))
        for i, account_info in enumerate(accounts):
            for mail in account_info[1:]:
                if mail not in mail_to_ind:
                    mail_to_ind[mail] = i
                else:
                    ds.unionBySize(mail_to_ind[mail], i)

        ans = [[] for i in range(len(accounts))]

        for mail in list(mail_to_ind.keys()):
            # print(mail, ds.parent[mail_to_ind[mail]])
            root = ds.findUPar(mail_to_ind[mail])
            ans[root].append(mail)

        ans_final = []

        for i, row in enumerate(ans):
            if row != []:
                ans_temp = [accounts[i][0]] + sorted(row)
                ans_final.append(ans_temp)

        return ans_final


s = Solution()

k1 = s.accountsMerge(
    [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
)

k2 = s.accountsMerge(
    [
        ["John", "j1@com", "j2@com", "j3@com"],
        ["John", "j4@com"],
        ["Raj", "r1@com", "r2@com"],
        ["John", "j1@com", "j5@com"],
        ["Raj", "r2@com", "r3@com"],
        ["Mary", "m1@com"],
    ]
)

k3 = s.accountsMerge(
    [
        [
            "opidgzg",
            "ayekp@gmail.com",
            "uq@gmail.com",
            "xto@gmail.com",
            "jb@gmail.com",
            "vh@gmail.com",
            "f@gmail.com",
            "higtc@gmail.com",
        ],
        [
            "hbbf",
            "i@gmail.com",
            "d@gmail.com",
            "qs@gmail.com",
            "bp@gmail.com",
            "ku@gmail.com",
        ],
        ["lvflofp", "wz@gmail.com", "zqibi@gmail.com"],
        [
            "tjlkno",
            "fdus@gmail.com",
            "j@gmail.com",
            "v@gmail.com",
            "zvmlb@gmail.com",
            "kefas@gmail.com",
        ],
        [
            "xrk",
            "ws@gmail.com",
            "om@gmail.com",
            "duc@gmail.com",
            "jpz@gmail.com",
            "c@gmail.com",
        ],
        ["hspt", "trhu@gmail.com", "k@gmail.com", "aulab@gmail.com"],
        [
            "xrk",
            "r@gmail.com",
            "b@gmail.com",
            "kg@gmail.com",
            "vt@gmail.com",
            "kfqi@gmail.com",
            "s@gmail.com",
            "kdbqj@gmail.com",
            "om@gmail.com",
            "zj@gmail.com",
        ],
        [
            "dl",
            "ggkx@gmail.com",
            "lee@gmail.com",
            "mhmr@gmail.com",
            "qascu@gmail.com",
            "n@gmail.com",
            "svpld@gmail.com",
            "rxval@gmail.com",
            "vnlru@gmail.com",
            "zr@gmail.com",
        ],
        [
            "xrk",
            "gnkzq@gmail.com",
            "iug@gmail.com",
            "yqhqy@gmail.com",
            "fxmw@gmail.com",
            "q@gmail.com",
            "pdd@gmail.com",
            "spau@gmail.com",
        ],
        ["wasovc", "qxr@gmail.com", "btms@gmail.com"],
        [
            "xrk",
            "q@gmail.com",
            "u@gmail.com",
            "auujy@gmail.com",
            "x@gmail.com",
            "plx@gmail.com",
            "ywq@gmail.com",
            "b@gmail.com",
            "ynpx@gmail.com",
        ],
        [
            "zl",
            "kkbz@gmail.com",
            "lvrve@gmail.com",
            "drvg@gmail.com",
            "ghepg@gmail.com",
            "prl@gmail.com",
            "y@gmail.com",
        ],
        ["vhkjt", "zgg@gmail.com", "m@gmail.com"],
        [
            "opidgzg",
            "kpl@gmail.com",
            "zuas@gmail.com",
            "bjqov@gmail.com",
            "vly@gmail.com",
            "xto@gmail.com",
            "jb@gmail.com",
            "gpuz@gmail.com",
            "higtc@gmail.com",
            "cki@gmail.com",
        ],
    ]
)

print(k1)
print(k2)
print(k3)
