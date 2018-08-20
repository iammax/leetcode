class Solution(object):
    def isPalindrome(self, x):
        st = str(x)
        if st == st[::-1]:
            return True
        else:
            return False
