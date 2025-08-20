class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        arr = [0]*len(s)
        st = ''
        for left, right, direc in shifts:
            if direc == 0:
                arr[left] -= 1
                if right < len(s)-1:
                    arr[right+1] += 1
            else:
                arr[left] += 1
                if right < len(s)-1:
                    arr[right+1] -= 1

        for i in range(len(arr)):
            if i != 0:
                arr[i] += arr[i-1]

        for i in range(len(s)):
            st += chr(((ord(s[i]) - ord('a') + arr[i])%26) + ord('a'))
        
        return st
        
        
            

   

                
        