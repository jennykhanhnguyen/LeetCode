class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = []
        for i in range(len(edges)):
            rep.append(i)
        size = [1]*len(edges)

        def find(u):
            if u == rep[u]:
                return u
            else:
                rep[u] = find(rep[u])
                return rep[u]
        def combine(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return True
            else:
                if size[u] > size[v]:
                    rep[v] = u
                    size[u] += size[v]
                else:
                    rep[u] = v
                    size[v] += size[u]
            return False

        for left, right in edges:
            redundant = combine(left-1, right-1)
            if redundant == True:
                return [left, right]
        return []