class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = []
        for num in nums:
            out.append(nums[num])
        return out
