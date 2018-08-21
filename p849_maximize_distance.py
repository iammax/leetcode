class Solution(object):
    def maxDistToClosest(self, seats):
        leftlist = []
        rightlist = []
        all_list = []
        dim = len(seats)
        leftcount = dim+1
        leftpos = 0
        rightcount = dim+1
        while leftpos < dim:
            rightpos = dim - leftpos -1
            if seats[leftpos] == 1:
                leftcount = 0
            else:
                leftcount += 1
            if seats[rightpos] == 1:
                rightcount = 0
            else:
                rightcount += 1
            leftlist.append(leftcount)
            rightlist.append(rightcount)
            leftpos += 1
        counter = 0
        rightlist = rightlist[::-1]
        best = 0
        while counter < dim:
            left = leftlist[counter]
            right = rightlist[counter]
            thisone = min(left, right)
            if thisone > best:
                best = thisone
            counter +=1
        return best
