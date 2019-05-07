class Solution(object):
    def containsDuplicate(self, nums):
        s = sorted(nums)
        dim = len(s)
        counter = 1
        if len(nums) == 0:
            return False
        prevnum = s[0]
        while counter < dim:
            thisnum = s[counter]
            if thisnum == prevnum:
                return True
            counter += 1
            prevnum = thisnum
        return False
