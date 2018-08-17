class Solution(object):
    def fizzBuzz(self, n):
        out = []
        for q in range (1, n+1):
            if q%15 == 0:
                out.append('FizzBuzz')
            elif q%5 == 0:
                out.append('Buzz')
            elif q%3 == 0:
                out.append('Fizz')
            else:
                out.append(str(q))
        return out
