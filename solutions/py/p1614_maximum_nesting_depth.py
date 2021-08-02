class Solution(object):
    def maxDepth(self, s):
        depth = 0
        maxdepth = 0
        for char in s:
            if char == '(':
                depth += 1
                if depth > maxdepth:
                    maxdepth = depth
            elif char == ')': 
                depth -= 1
        return maxdepth
