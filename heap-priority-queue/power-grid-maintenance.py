from collections import defaultdict
import heapq
# by default: min heap
class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # rep[u]
        # size[u]
        status = [1]*(c+1) # 1 is online
        rep = []
        size = [1]*(c+1)
        dsu = defaultdict(list)
        ans = []

        for i in range(c+1):
            rep.append(i)

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

        for ind,tple in enumerate(connections):
            left = tple[0]
            right = tple[1]
            combine(left, right)

        for ind, station in enumerate(rep):
            heapq.heappush(dsu[find(ind)],ind)
        # print(dsu)
        # return []

        for ind,tple in enumerate(queries):
            left = tple[0]
            right = tple[1]
            if left == 1:
                if status[right] == 1:
                    ans.append(right)
                else:
                    if len(dsu[rep[right]]) == 0:
                        ans.append(-1)
                    else:
                        ans.append(dsu[rep[right]][0])
            elif left == 2:
                heapq.heappop(dsu[find(right)])
                status[right] = 0

        return ans

