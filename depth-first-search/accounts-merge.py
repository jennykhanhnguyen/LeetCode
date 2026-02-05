from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def find(x):
            if x == rep[x]:
                return x
            else:
                rep[x] = find(rep[x])
                return rep[x]
        def combine(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            else:
                if size[u] > size[v]:
                    rep[v] = u
                    size[u] += size[v]
                else:
                    rep[u] = v
                    size[v] += size[u]
        rep = defaultdict(str)
        size = defaultdict(int)
        for i, lsti in enumerate(accounts):
            for k in range(1,len(lsti)):
                rep[i] = i
                size[i] = 1

        # print(rep)

        # set for each list
        for i, lsti in enumerate(accounts):
            if i+1 <= len(accounts):
                for j in range(i+1, len(accounts)):
                    lstj = accounts[j]
                    # print(i,j)
                    if lsti[0] == lstj[0]:
                        # print(lsti,lstj)
                        setlstj = set(lstj[1:])
                        # print(setlstj)
                        for k in range(1, len(lsti)):
                            if lsti[k] in setlstj:
                                # elmt = setlstj.pop()
                                # while lsti[k] == elmt:
                                #     elmt = setlstj.pop()   
                                # print(lsti[k], setlstj)
                                # print(rep[lsti[k]], j)                  
                                combine(i, j)
        # print(rep)

        ans = defaultdict(set)
        for key, val in rep.items():
            temp = accounts[key][1:]
            for i in range(len(temp)):
                ans[find(val)].add(temp[i])

        finalans = []
        for key, val in ans.items(): # key: index of parent, val: set of emails
            temp = list(val)
            temp.sort()
            name = [accounts[key][0]]
            adding = name + temp 
            finalans.append(adding)
            finalans.sort()
        return finalans
        # return []
                