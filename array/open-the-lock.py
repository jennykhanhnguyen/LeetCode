import queue
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = queue.Queue()

        q.put(0)
        # N -> số lượng đỉnh
        # 10^4 = 10000
        flag = [False for i in range(10**4)] 
        flag[0] = True
        for x in deadends:
            if int(x) == 0:
                return -1
            flag[int(x)] = True
        # flag = set()
        # graph -> graph
        target = int(target)
        cnt = 0
        while q.qsize() > 0:
            for _ in range(q.qsize()):
                u = q.get()
                if u == target:
                    return cnt
                # '0000'
                u = list(str(u).zfill(4)) # ['0', '0', '0', '1']
                for i in range(4):
                    u[i] = str((int(u[i]) - 1) % 10)
                    v = int(''.join(u))
                    if flag[v] == False:
                        q.put(v)
                        flag[v] = True

                    u[i] = str((int(u[i]) + 2) % 10)
                    v = int(''.join(u))
                    if flag[v] == False:
                        q.put(v)
                        flag[v] = True

                    u[i] = str((int(u[i]) - 1) % 10)
                # 0 -> 1, 2
                # 1, 2 -> 3, 4, 5
                # 3, 4, 5
            cnt += 1
        return -1