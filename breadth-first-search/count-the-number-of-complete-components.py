class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(set)
        for ind, tple in enumerate(edges):
            graph[tple[0]].add(tple[1])
            graph[tple[1]].add(tple[0])
        rep = []
        for i in range(n):
            rep.append(i)
        size = [1]*n
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
                return
            else:
                if size[u] > size[v]:
                    rep[v] = u
                    size[u] += size[v]
                else:
                    rep[u] = v
                    size[v] += size[u]
        for ind, tple in enumerate(edges):
            combine(tple[0], tple[1])
        # print(rep,size)
       
        for node in range(n): # order matters in dsu
            find(node)

        set_rep = set(rep)
        # print(rep,size)
        ans = 0
        cnt_edge = defaultdict(int)
        for left, right in edges:
            cnt_edge[rep[left]] += 1
        for head in set_rep:
            n = size[head] 
            if cnt_edge[head] == (n*(n-1))/2:
                ans += 1
        return ans