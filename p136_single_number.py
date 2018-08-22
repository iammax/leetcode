class Solution(object):
    def singleNumber(self, nums):
        tl = []
        for q in sorted(nums):
            if q not in tl:
                tl.append(q)
            else:
                tl.remove(q)
        return tl[0]
