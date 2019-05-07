class Solution(object):
    def repeatedNTimes(self, A):
        used = []
        for item in A:
            if item not in used:
                used.append(item)
            else:
                return item
