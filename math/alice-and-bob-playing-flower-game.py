class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddn = int(n/2 if n%2 == 0 else n//2+1)
        evenn = int(n/2 if n%2 == 0 else n//2)

        oddm = int(m/2 if m%2 == 0 else m//2+1)
        evenm = int(m/2 if m%2 == 0 else m//2)

        return oddn*evenm+oddm*evenn