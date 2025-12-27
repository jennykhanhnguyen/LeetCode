from collections import defaultdict, deque
from typing import List

class Solution:
    def _build_graph(self, pairs, rates):
        g = defaultdict(list)
        for (a, b), r in zip(pairs, rates):
            g[a].append((b, r))
            g[b].append((a, 1.0 / r))
        return g

    def _bfs_factors(self, g, start):
        # returns: factor[start->node]
        factor = {start: 1.0}
        q = deque([start])

        while q:
            cur = q.popleft()
            for nxt, w in g[cur]:
                if nxt not in factor:
                    factor[nxt] = factor[cur] * w
                    q.append(nxt)
        return factor

    def maxAmount(self, initialCurrency: str,
                       pairs1: List[List[str]], rates1: List[float],
                       pairs2: List[List[str]], rates2: List[float]) -> float:

        g1 = self._build_graph(pairs1, rates1)
        g2 = self._build_graph(pairs2, rates2)

        f1 = self._bfs_factors(g1, initialCurrency)  # initial -> c on day1
        f2 = self._bfs_factors(g2, initialCurrency)  # initial -> c on day2

        best = 1.0  # do nothing
        for c, amt_in_c_after_day1 in f1.items():
            if c in f2:
                # on day2 convert c -> initial
                c_to_initial_day2 = 1.0 / f2[c]
                best = max(best, amt_in_c_after_day1 * c_to_initial_day2)

        return best
