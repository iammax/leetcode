class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        counter = 0
        while counter < num:
            squared = counter*counter
            if squared == num:
                return True
            if squared > num:
                return False
            counter += 1
