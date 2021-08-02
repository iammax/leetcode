class Solution(object):
    def shuffle(self, nums, n):
        out = []
        for q in range (0, n):
            out.append(nums[q])
            out.append(nums[q+n])
        return out
