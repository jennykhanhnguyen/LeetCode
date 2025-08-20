class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lst = [0 for i in range(len(words))]
        result = []
        for i in range (len(words)):
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                lst[i] = 1
            else:
                lst[i] = 0
            if i != 0:
                lst[i] += lst[i-1]
        for left,right in queries:
            if left == 0: 
                result.append(lst[right])
            else:
                result.append(lst[right] - lst[left-1])

        return result