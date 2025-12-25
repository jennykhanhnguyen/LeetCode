from collections import deque, defaultdict
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        queue.append(id)
        visited = set([id])

        lv = -1
        lst = []
        while queue:
            lv += 1
            size = len(queue)
            if lv == level:
                for i in range(size):
                    lst.append(queue.popleft())
                break   
            for i in range(size):
                node = queue.popleft()
                for nei in friends[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        dct = defaultdict(int)
        for friend in lst:
            for item in watchedVideos[friend]:
                dct[item]+= 1
        sorted_items = sorted(dct.items(), key=lambda item: (item[1], item[0]))
        return [video for video, freq in sorted_items]
        

