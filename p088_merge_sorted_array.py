class Solution(object): #this is sort of a workaround, make it more in the spirit of the problem later. it still works though!
    def merge(self, nums1, m, nums2, n):
        newl = []
        for q in range (0, m):
            newl.append(nums1[q])
        for q in range (0, n):
            newl.append(nums2[q])
        counter = 0
        newl = sorted(newl)
        while counter < m + n:
            nums1[counter] = newl[counter]
            counter += 1
