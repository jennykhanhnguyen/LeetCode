class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        path = []
        setnums = set(nums)
        lstt = ['0','1']
        def backtrack(index):
            if index == n:
                final = ''.join(path)
                if final not in setnums:
                    return final
                return None
            for i, num in enumerate(lstt):
                path.append(num)
                res = backtrack(index+1)
                if res:
                    return res
                path.pop()
        return backtrack(0)