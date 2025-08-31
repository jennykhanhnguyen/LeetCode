class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        new = ''
        changed = False
        for i in range(len(num)):
            if num[i] == '9':
                new += num[i]
            elif num[i] != '9' and changed == False:
                new += '9'
                changed = True
        return int(new)