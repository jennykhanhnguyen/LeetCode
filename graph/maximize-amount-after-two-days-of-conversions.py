from collections import defaultdict  # defaultdict gives 0.0 for unseen currencies

class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """

        def build_edges(pairs, rates):
            edges = []                                  # store edges as (u, v, rate)
            for (u, v), r in zip(pairs, rates):         # loop through each given conversion
                edges.append((u, v, float(r)))          # forward edge u -> v
                edges.append((v, u, 1.0 / float(r)))    # inverse edge v -> u
            return edges                                # return full edge list

        def propagate_best(edges, best):
            currencies = set(best.keys())               # start with currencies we already track
            for u, v, r in edges:                       # collect all nodes appearing in edges
                currencies.add(u)                       # add start currency
                currencies.add(v)                       # add target currency
            currencies = list(currencies)               # convert set to list so we can count |V|

            # Bellman-Ford style relaxation: at most |V|-1 rounds to propagate along paths
            for _ in range(len(currencies) - 1):        # repeat enough times for longest simple path
                changed = False                         # track whether any update happened this round

                for u, v, r in edges:                   # try relaxing every edge
                    if best[u] == 0.0:                  # if u is unreachable, skip
                        continue                         # can't convert from a currency we don't have

                    candidate = best[u] * r             # amount in v if we convert u -> v
                    if candidate > best[v]:             # if this path improves best[v]
                        best[v] = candidate             # update best amount for currency v
                        changed = True                  # mark that we changed something

                if not changed:                         # if no edge improved anything
                    break                               # we already reached the maximums

            return best                                 # return updated best amounts

        edges1 = build_edges(pairs1, rates1)            # build day 1 edges (with inverses)
        edges2 = build_edges(pairs2, rates2)            # build day 2 edges (with inverses)

        best = defaultdict(float)                       # best[c] = max amount of currency c
        best[initialCurrency] = 1.0                     # start with 1.0 of initialCurrency

        best = propagate_best(edges1, best)             # do any number of conversions on day 1

        best = propagate_best(edges2, best)             # do any number of conversions on day 2

        return max(1.0, best[initialCurrency])          # doing nothing gives 1.0 baseline
