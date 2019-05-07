class Solution(object):
    def findTheDifference(self, s, t):
        slist = [q for q in s]
        for char in t:
            try:
                slist.remove(char)
            except:
                return char
