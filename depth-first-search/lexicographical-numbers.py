class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lst = []
        cur = 1
        while len(lst) < n:
            lst.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while (cur == n or cur%10 == 9):
                    cur = cur//10
                cur += 1
        return lst
