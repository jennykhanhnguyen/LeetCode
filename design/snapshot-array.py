from collections import defaultdict
import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.dct = defaultdict(list) # key = index, value = list of (snap_id, val)
        self.current_snap_id = 0
    def set(self, index: int, val: int) -> None:
        if len(self.dct[index]) != 0 and self.dct[index][-1][0] == self.current_snap_id:
            self.dct[index].pop()
        self.dct[index].append((self.current_snap_id, val)) 

    def snap(self) -> int: 
        self.current_snap_id += 1
        return self.current_snap_id -1

    def get(self, index: int, snap_id: int) -> int:
        # binary search
        position = bisect.bisect_right(self.dct[index], (snap_id, float("inf"))) - 1
        return self.dct[index][position][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)