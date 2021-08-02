def fact(x):
        if x > 1:
                return x*fact(x-1)
        else:
                return x

def choose2(n, r = 2):
    
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fact(n)/(fact(r)*fact(n-r))

class Solution(object):
    def numIdenticalPairs(self, nums):
        population = {}
        for num in nums:
            if num in population:
                population[num] += 1
            else:
                population[num] = 1
        total = 0
        for num in population:
            pop = population[num]
            total += choose2(pop)
        return total
