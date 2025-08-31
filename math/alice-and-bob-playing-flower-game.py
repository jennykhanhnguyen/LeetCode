class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddn = n//2 if n%2 == 0 else n//2+1
        evenn = n//2 if n%2 == 0 else n//2

        oddm = m//2 if m%2 == 0 else m//2+1
        evenm = m//2 if m%2 == 0 else m//2

        return oddn*evenm+oddm*evenn