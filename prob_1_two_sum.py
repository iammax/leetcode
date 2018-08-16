class Solution(object):
    def twoSum(self, nums, target):
        solution = None
        numlength = len(nums)
        for q in range (0, numlength-1):
            for r in range (q+1, numlength):
                if nums[q] + nums[r] == target:
                    solution = [q, r]
                    break
        return solution
