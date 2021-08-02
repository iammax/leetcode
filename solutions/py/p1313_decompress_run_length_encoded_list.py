class Solution(object):
    def decompressRLElist(self, nums):
        out = []
        counter = 0
        while counter < len(nums):
            freq = nums[counter]
            val = nums[counter+1]
            for  i in range (freq):
                out.append(val)
            counter += 2
        return out
