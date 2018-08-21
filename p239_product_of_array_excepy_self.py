class Solution(object):
    def productExceptSelf(self, nums):
        forwardlist = [1]
        backwardlist = [1]
        dim = len(nums)
        counter = 1
        while counter < dim:
            rightcounter = dim - counter
            forwardlist.append(forwardlist[counter-1]*nums[counter-1])
            backwardlist.append(backwardlist[counter-1]*nums[rightcounter])
            counter += 1
        result = []
        counter = 0
        while counter < dim:
            result.append(forwardlist[counter]*backwardlist[dim-1-counter])
            counter += 1
        return result
