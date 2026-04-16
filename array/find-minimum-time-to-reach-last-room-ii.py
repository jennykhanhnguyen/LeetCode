import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [ [ [float('inf')]*3 for _ in range(m)] for _ in range(n)]

        dist[0][0][1] = 0
        heap = []
        heapq.heappush(heap,(0, 0, 0, 1))  # time, row, col, nextCost

        dirr = [0,1,-1,0]
        dirc = [1,0,0,-1]



        while heap:
            time, r, c, nextCost = heapq.heappop(heap)

            if time > dist[r][c][nextCost]:
                continue

            for i in range(4):
                newr = r + dirr[i]
                newc = c + dirc[i]

                if newr < 0 or newr >= n or newc < 0 or newc >= m:
                    continue

                newTime = max(time, moveTime[newr][newc]) + nextCost
                nextNextCost = 2 if nextCost == 1 else 1

                if newTime < dist[newr][newc][nextNextCost]:
                    dist[newr][newc][nextNextCost] = newTime
                    heapq.heappush(heap, (newTime, newr, newc, nextNextCost))

        answer = min(dist[n-1][m-1][1], dist[n-1][m-1][2])
        return answer