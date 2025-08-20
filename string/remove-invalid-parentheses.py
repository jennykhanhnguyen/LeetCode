import queue
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        visited = set()
        q = queue.Queue()
        q.put(s)
        found = False
        result = []

        while not q.empty():
            curr = q.get()
            
            if self.isValid(curr):
                result.append(curr)
                found = True
            if found:
                continue  

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                next_state = curr[:i] + curr[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    q.put(next_state)
        return result

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
