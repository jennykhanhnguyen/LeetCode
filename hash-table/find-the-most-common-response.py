class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        lst = []
        for respon in responses:
            res = set()
            for r in respon:
                if r not in res:
                    res.add(r)
            lst.append(res)
            
        dic = {}
        for sett in lst:
            for word in sett:
                dic[word] = dic.get(word,0) + 1
        
        maxval = 0
        maxword = ''
        for key, val in dic.items():
            if val > maxval:
                maxword = key
                maxval = val
            if val == maxval:
                maxword = min (key,maxword)

        return maxword

