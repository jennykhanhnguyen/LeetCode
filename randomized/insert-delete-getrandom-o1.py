import random
class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.hm = {}

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        else:
            self.lst.append(val)
            self.hm[val] = len(self.lst)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        else:
            idrm = self.hm[val]
            numswap = self.lst[-1]
            self.lst[idrm], self.lst[-1] = self.lst[-1], self.lst[idrm]
            self.hm[numswap] = idrm
            self.hm.pop(val, None)
            self.lst.pop()
            return True

    def getRandom(self) -> int:
        random_val = random.randint(0, len(self.lst)-1)
        return self.lst[random_val]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()