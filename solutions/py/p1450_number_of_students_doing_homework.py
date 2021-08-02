class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        numstudents = len(startTime)
        doingHW = 0
        for student in range(numstudents):
            if queryTime >= startTime[student] and queryTime <= endTime[student]:
                doingHW += 1
        return doingHW
