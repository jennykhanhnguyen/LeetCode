class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        d = {}
        for w in wordlist:
            tmp = w.lower()
            # print(tmp, w)
            if tmp not in d:
                d[tmp] = w

        d2 = {}
        for w in wordlist:
            tmp = w.lower().replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')
            if tmp not in d2:
                d2[tmp] = w
        ans = []
        for q in queries:
            tmp = q.lower()
            if q in wordlist:
                ans.append(q)
            elif tmp in d:
                ans.append(d[tmp])
            elif tmp.replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a') in d2:
                ans.append(d2[tmp.replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')])
            else:
                ans.append("")
        return ans


     