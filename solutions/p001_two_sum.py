class Solution(object):
    def twoSum(self, nums, target):
        orignums = nums
        nums = sorted(nums)
        numlength = len(nums)
        for q in range (0, numlength-1):
            qnum = nums[q]
            want = target - qnum
            rcount = q+1
            while rcount < numlength:
                rnum = nums[rcount]
                if  rnum == want:
                    if qnum != rnum:
                        return [orignums.index(qnum), orignums.index(rnum)]
                    else:
                        qindex = orignums.index(qnum)
                        dim = len(orignums)
                        newrcount = qindex+1
                        while True:
                            if orignums[newrcount] == rnum:
                                return [qindex, newrcount]
                            newrcount += 1
                elif rnum > want:
                    rcount = numlength
                rcount += 1
        
