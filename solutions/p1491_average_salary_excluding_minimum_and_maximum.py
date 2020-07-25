class Solution(object):
    def average(self, salary):
        return sum(sorted(salary)[1:-1])/float((len(salary)-2))
