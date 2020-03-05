class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        out = []
        dim = len(nums)
        sort = sorted(nums)
        out_dict = {sort[0]:0}
        prev_num = sort[0]
        counter = 1
        while counter < dim:
            here = sort[counter]
            if here not in out_dict:
                out_dict[here] = counter
            counter += 1
        for num in nums:
            out = out + [out_dict[num]]
        return out
