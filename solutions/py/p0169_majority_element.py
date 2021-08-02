class Solution(object):
    def majorityElement(self, nums):
        dim = len(nums)
        if dim == 1:
            return nums[0]
        cutoff = dim/2
        counts = {}
        for num in nums:
            if num in counts:
                if counts[num] == cutoff:
                    return num
                else:
                    counts[num] += 1
            else:
                counts[num] = 1
            
        
