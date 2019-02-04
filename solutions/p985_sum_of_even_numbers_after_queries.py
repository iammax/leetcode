class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        out = []
        total = 0
        for q in A:
            if q%2 == 0:
                total += q
        for query in queries:
            index = query[1]
            val = A[index]
            addition = query[0]
            newval = val + addition
            A[index] = newval
            if val % 2 == 0:
                if addition % 2 == 0:
                    total += addition
                else:
                    total -= val
            else:
                if addition %2 == 0:
                    pass
                else:
                    total += newval
            out.append(total)
        return out
