from math import gcd
import heapq
from typing import List

class Frac:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = numerator
        self.den = denominator

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"
    
    def __sub__(self, other):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

        return Frac(self.num * other.den - other.num * self.den,
                    self.den * other.den)

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den
    
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        total = 0
        for i in range(len(classes)):
            heapq.heappush(heap, (
                Frac(classes[i][0], classes[i][1]) - Frac(classes[i][0] + 1, classes[i][1] + 1),
                Frac(classes[i][0], classes[i][1])
            ))
        for student in range(extraStudents):
            ans = heapq.heappop(heap)         
            ansn = ans[1].num + 1
            ansd = ans[1].den + 1
            heapq.heappush(heap, (
                Frac(ansn, ansd) - Frac(ansn + 1, ansd + 1),
                Frac(ansn, ansd)
            ))
        for i in range(len(classes)):    
            ans = heapq.heappop(heap)         
            ansn = ans[1].num
            ansd = ans[1].den
            total += ansn / ansd
        return total / len(classes)
