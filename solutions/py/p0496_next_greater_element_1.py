class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        out = [-1]*len(nums1)
        len_nums2 = len(nums2)
        index1 = 0
        while index1 < len(nums1):
            num1 = nums1[index1]
            index2 = nums2.index(num1)+ 1
            while index2 < len_nums2:
                num2 = nums2[index2]
                if num2 > num1:
                    out[index1] = num2
                    index2 = len_nums2
                index2 += 1
            index1 += 1
        return out
