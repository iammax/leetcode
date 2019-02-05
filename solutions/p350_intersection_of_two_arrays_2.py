#The longer code is much faster but requires more memory

class Solution(object):
    def intersect(self, nums1, nums2):
        out = []
        def counter(nums):
            counts = {}
            for q in nums:
                if q in counts:
                    counts[q] += 1
                else:
                    counts[q] = 1
            return counts
        
        def comparison(shorter, longer):
            out = []
            for item in shorter:
                if item in longer:
                    shorter_count = shorter[item]
                    longer_count = longer[item]
                    intersect = min(shorter_count, longer_count)
                    for q in range(intersect):
                        out.append(item)
            return out
            
        counts_1 = counter(nums1)
        counts_2 = counter(nums2)
        if len(counts_1) > len(counts_2):
            return comparison(counts_2, counts_1)
        else:
            return comparison(counts_1, counts_2)

#class Solution(object):
#    def intersect(self, nums1, nums2):
#        out = []
#        for item in nums1:
#            if item not in out:
#                count_1 = nums1.count(item)
#                count_2 = nums2.count(item)
#                for count in range(min(count_1,count_2)):
#                    out.append(item)
#        return out
