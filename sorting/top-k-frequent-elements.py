class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        lst = []
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            elif nums[i] in hm:
                hm[nums[i]] += 1
        sorted_val = sorted(hm.values(), reverse = True)
        maxx_freq = sorted_val[k-1]
        for tup in hm:
            if hm[tup] >= maxx_freq:
                lst.append(tup)
        return lst
