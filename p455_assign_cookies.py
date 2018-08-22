class Solution(object):
    def findContentChildren(self, g, s):
        out = 0
        g = sorted(g)
        s = sorted(s)
        for child in g:
            for cookie in s:
                if cookie >= child:
                    out += 1
                    s.remove(cookie)
                    break
        return out
