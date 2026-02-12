class Bitset:

    def __init__(self, size: int): 
        self.res = [0] * size
        
        self.setA = set() # set of indicies of bit 0
        for i in range(size):
            self.setA.add(i)
        self.setB = set() # set of indicies of bit 0

        self.zeros = True # True: setA -- 0
        self.size = size

    def fix(self, idx: int) -> None: # O(1)
        if self.zeros == True: # True: setA -- 0
            if idx in self.setA:
                self.setA.remove(idx)
            if idx not in self.setB:
                self.setB.add(idx)
        else:
            if idx in self.setB:
                self.setB.remove(idx)
            if idx not in self.setA:
                self.setA.add(idx)

    def unfix(self, idx: int) -> None: # O(1)    
        if self.zeros == False: # False: setA -- 1
            if idx in self.setA:
                self.setA.remove(idx)
            if idx not in self.setB:
                self.setB.add(idx)
        else:
            if idx in self.setB:
                self.setB.remove(idx)
            if idx not in self.setA:
                self.setA.add(idx)
    def flip(self) -> None: # O(n) --> O(1)/ log
        if self.zeros == True:
            self.zeros = False
        else:
            self.zeros = True

    def all(self) -> bool: # O(n) --> O(1)/ log
        if self.zeros == True: # True: setA -- 0
            return len(self.setA) == 0
        else: 
            return len(self.setB) == 0

    def one(self) -> bool: # O(n) --> O(1)/ log
        if self.zeros == True: # True: setA -- 0
            return len(self.setB) > 0
        else: 
            return len(self.setA) > 0

    def count(self) -> int: # O(n) --> O(1)/ log
        if self.zeros == True: # True: setA -- 0
            return len(self.setB)
        else: 
            return len(self.setA)

    def toString(self) -> str: # O(n)
        lst = []
        if self.zeros == True: # True: setA -- 0
            for i in range(self.size):
                if i in self.setA: # bit 0
                    lst.append(0)
                else:
                    lst.append(1)
        else: 
            for i in range(self.size):
                if i in self.setB: # bit 0
                    lst.append(0)
                else:
                    lst.append(1)
        s= ''.join(str(digit) for digit in lst)
        return s


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()