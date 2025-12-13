class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        final = []
        n = 2*n
        res = []
        def recur(ind):
            # print(lst, ind, n)
            if ind == n:
                stringg = "".join(lst.copy())
                final.append(stringg)
            if ind == n:
                return 
            for j in range (2):
                if j == 0:
                    char = '('
                else:
                    char = ')'
                lst.append(char)
                recur(ind+1)
                lst.pop()
        recur(0)
        def validParen(word):
            stack = []
            for s in word:
                if s == '(':
                    stack.append(s)
                elif s == ')' and len(stack) != 0:
                    stack.pop()
                else: # s == ') and len(stack) == 0
                    return False
            return len(stack) == 0

        for paren in final:
            if validParen(paren) == True:
                res.append(paren)

        return res