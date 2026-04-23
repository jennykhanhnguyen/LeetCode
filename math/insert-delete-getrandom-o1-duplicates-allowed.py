from collections import defaultdict
import random 
class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.hm = defaultdict(set)

    def insert(self, val: int) -> bool:
        boolean = True
        if val in self.hm and len(self.hm[val]) != 0:
            boolean = False
        self.lst.append(val)
        self.hm[val].add(len(self.lst)-1)
        print(val, self.hm)
        return boolean

    def remove(self, val: int) -> bool:
        if val not in self.hm or len(self.hm[val]) == 0 or len(self.lst) == 0:
            return False
        if len(self.lst) == 1:
            self.hm[self.lst[-1]].pop()
            self.lst.pop()
            return True
        index_rm = self.hm[val].pop()
        last_num = self.lst[-1] 
        index_last_num = len(self.lst) -1
        self.lst[-1], self.lst[index_rm] = self.lst[index_rm],self.lst[-1]
        print(last_num,self.hm[last_num])
        self.hm[last_num].remove(index_last_num)
        self.hm[last_num].add(index_rm)
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.lst)-1)
        return self.lst[rand]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()