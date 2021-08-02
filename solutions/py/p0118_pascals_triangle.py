class Solution(object):
    def generate(self, numRows):
        output = []
        for n in range (0, numRows):
            line = []
            for k in range (0, n/2+1):
                line.append(choose(n,k))
            if n%2 == 0:
                for q in line[:-1][::-1]:
                    line.append(q)
            else:
                for q in line[::-1]:
                    line.append(q)
            output.append(line)
            
        return output

def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def factorial(x):
    total = 1
    while x > 1:
        total *= x
        x -= 1
    return total
