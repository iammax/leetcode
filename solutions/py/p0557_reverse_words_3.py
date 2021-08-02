class Solution(object):
    def reverseWords(self, s):
        line = s.split()
        return ' '.join([q[::-1] for q in line])
        
