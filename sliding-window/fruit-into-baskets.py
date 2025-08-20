class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        arr = [0]*len(fruits)
        l = 0
        r = 0
        cnt = 0  
        maxval = 1
        while r < len(fruits):
            arr[fruits[r]] += 1
            if arr[fruits[r]] == 1:
                cnt += 1
                while cnt > 2:
                    arr[fruits[l]] -= 1
                    if arr[fruits[l]] == 0:
                        cnt -= 1
                    l += 1
            maxval = max(maxval, r-l+1)
            r += 1
        return maxval

    
