class Solution(object):
    def xorOperation(self, n, start):
        nums = []
        for i in range (0, n):
            nums.append(start + 2*i)
        out = nums[0]
        for num in nums[1:]:
            out = out ^ num
        return out
