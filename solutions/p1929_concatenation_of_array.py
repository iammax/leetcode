class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #lazy solution
        #out = []
        #for q in range(2):
#            for num in nums:
#                out.append(num)

        #slightly better performance solution
        dim = len(nums)
        out = [0]*(2*dim)
        for i in range(dim):
            num = nums[i]
            out[i] = num
            out[dim + i] = num
        return out
