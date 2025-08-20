class Solution:
    def maxDiff(self, num: int) -> int:
        str1 = str(num)
        tmp1 = '9'
        if str1[0] == '9':
            for i in range (len(str1)):
                if str1[i] != '9':
                    tmp1 = str1[i]
                    break
            str1 = str1.replace(tmp1, '9')

        else:
            str1 = str1.replace(str1[0], '9')

        tmp2 = ''
        str2 = str(num)
        if str2[0] == '1':
            for i in range (len(str2)):
                if str2[i] != '1' and str2[i] != '0':
                    tmp2 = str2[i]
                    break
            if tmp2 != '':
                str2 = str2.replace(tmp2, '0')

        else:
            str2 = str2.replace(str2[0], '1')

        int1 = int(str1)
        int2 = int(str2)
        return int1 - int2


