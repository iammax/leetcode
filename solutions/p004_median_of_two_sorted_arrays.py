class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        list1 = nums1
        list2 = nums2
        len1 = len(list1)
        len2 = len(list2)

        index1 = 0
        index2 = 0
        newlist = []
        if len1 > 0:
            first = list1[0]
        if len2 > 0:
            second = list2[0]
    
        while index1 < len1 and index2 < len2: 
            greaterone = first > second #1 means first is bigger, 0 means second
            if greaterone: #list 1 val is bigger, so add from list 2
                firstval = list1[index1]
                while index2 < len2 and list2[index2] <= firstval:
                    second = list2[index2]
                    newlist.append(second)
                    index2 += 1

            else:
                secondval = list2[index2]
                while index1 < len1 and list1[index1] <= secondval:
                    firstval = list1[index1]
                    newlist.append(firstval)
                    index1 += 1
            if index1 < len1:
                first = list1[index1]
            if index2 < len2:
                second = list2[index2]

        while index1 < len1:
            newlist.append(list1[index1])
            index1 += 1
        while index2 < len2:
            newlist.append(list2[index2])
            index2 += 1

        length =  len1 + len2
        
        if length % 2 == 1:
            return newlist[length/2]
        else:

            return (newlist[length/2] + newlist[length/2 -1])/2.
