class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        superset = {}
        for domino in dominoes:
            x, y = domino[0], domino[1]
            small, large = min(x, y), max(x, y)
            if small in superset:
                if large in superset[small]:
                    superset[small][large] += 1
                else:
                    superset[small][large] = 1
            else:
                superset[small] = {}
                superset[small][large] = 1
        total = 0
        for smaller in superset:
            this_set = superset[smaller]
            for larger in this_set:
                total += choosetwo(this_set[larger])
        return total
def choosetwo(x):
    return (x)*(x-1)/2
