class Solution(object):
    def maximumSwap(self, num):
        digits = map(int,list(str(num)))
        results = swapper(digits, [])
        print 'results: ', results
        if results == map(int,list(str(num))):
            print 'same as: '
            return num
        else:
            out = ''
            for digit in results:
                out += str(digit)
            return int(out)
def swapper(digits, beginning):
    print 'running: digits, beginning: ', digits, beginning
    if len(digits) > 0:
        
        if digits.index(max(digits)) == 0:
            beginning.append(digits[0])
            print 'iterating: digits, beginning = ', digits[1:], beginning
            return swapper(digits[1:], beginning)
        else:
            maximum = max(digits)
            counter = 0
            dim = len(digits)
            indices = []
            occurences = digits.count(maximum)
            if occurences > 1:
                found = 0
                while found < occurences:
                    here = digits[counter]
                    if here == maximum:
                        indices.append(counter)
                        found += 1
                    counter += 1
                lastmax = indices[-1]
            else:
                lastmax = digits.index(maximum)
            digits[lastmax], digits[0] = digits[0], max(digits)
            return beginning + digits
    else:
        return beginning + digits
        
