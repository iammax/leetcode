class Solution(object):
    def customSortString(self, S, T):
        Tlist = list(T)
        out = ''
        for s in S:
            if s in Tlist:
                nums = Tlist.count(s)
                counter = 0
                while counter < nums:
                    out += s
                    Tlist.remove(s)
                    counter += 1
        for q in S:
            try:
                Tlist.remove(q)
            except:
                pass
        for t in Tlist:
            out += t
        return out
