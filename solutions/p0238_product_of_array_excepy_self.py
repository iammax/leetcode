class Solution(object):
    def productExceptSelf(self, nums):
        forwardlist = [1]
        backwardlist = [1]
        dim = len(nums)
        counter = 1
        while counter < dim:
            rightcounter = dim - counter
            forwardlist.append(forwardlist[counter-1]*nums[counter-1])
            counter += 1
        result = []
        counter = 0
        backthing = 1
        while counter < dim:
            if counter > 0:
                backthing *= nums[dim-counter]
            result.append(forwardlist[dim-1-counter]*backthing)
            counter += 1
        return result[::-1]
