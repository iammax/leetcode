class Solution(object):
    def singleNonDuplicate(self, nums):
        counter = 1
        dim = len(nums)
        while counter < dim:
            if nums[counter] == nums[counter-1]:
                newone = 1
            else:
                if counter == 1 or newone == 0:
                    return nums[counter-1]
                else:
                    newone = 0
            counter += 1
        return nums[-1]
                
