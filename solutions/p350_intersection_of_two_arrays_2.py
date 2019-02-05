class Solution(object):
    def intersect(self, nums1, nums2):
        out = []
        for item in nums1:
            if item not in out:
                count_1 = nums1.count(item)
                count_2 = nums2.count(item)
                for count in range(min(count_1,count_2)):
                    out.append(item)
        return out
