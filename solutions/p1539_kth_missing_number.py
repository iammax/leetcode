class Solution(object):
    def findKthPositive(self, arr, k):
        candidates = range(1, arr[-1] + k+1)
        for num in arr:
            candidates.remove(num)
        return candidates[k-1]
