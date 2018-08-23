class Solution(object):
    def intersection(self, nums1, nums2):
        out = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        for q in nums1:
            if q not in out:
                if q in nums2:
                    out.append(q)
        return out
