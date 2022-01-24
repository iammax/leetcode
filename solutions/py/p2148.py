class Solution(object):
    def countElements(self, nums):
        ma = max(nums)
        mi = min(nums)
        hits = 0
        for num in nums:   
            if mi < num and num < ma:
                hits += 1
        return hits
