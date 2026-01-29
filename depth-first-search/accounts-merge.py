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
        name = defaultdict(str)
        for i, lsti in enumerate(accounts):
            for k in range(1,len(lsti)):
                rep[accounts[i][k]] = accounts[i][1]
                size[accounts[i][k]] = 1
                name[accounts[i][k]] = accounts[i][0]

        # print(rep)

        # set for each list
        for i, lsti in enumerate(accounts):
            if i+1 <= len(accounts):
                for lstj in accounts[i+1:]:
                    if lsti[0] == lstj[0]:
                        # print(lsti,lstj)
                        setlstj = set(lstj[1:])
                        # print(setlstj)
                        for k in range(1, len(lsti)):
                            if lsti[k] in setlstj:
                                elmt = setlstj.pop()
                                while lsti[k] == elmt:
                                    elmt = setlstj.pop()    
                                # print(lsti[k], elmt)                    
                                combine(lsti[k], elmt)

        ans = defaultdict(list)
        anslst = []
        for key, val in rep.items(): # key: email, val: rep
            ans[find(key)].append(key)

        for key, vallst in ans.items():
            k = name[key]
            each = []           
            for item in vallst:
                each.append(item)
            each.sort()
            each = [k]+each
            anslst.append(each)
        # print(rep)
        # print(ans)
        # print(anslst)
        
        return anslst
                


        