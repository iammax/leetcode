class Solution(object):
    def romanToInt(self, s):
        total = 0
        dim = len(s)
        counter = 0
        while counter < dim:
            thisone = s[counter]
            if thisone == 'M':
                total += 1000
            elif thisone == 'D':
                total += 500
            elif thisone == 'C':
                if counter+1  < dim and s[counter+1] == 'D':
                    total += 400
                    counter += 1
                elif counter+1 < dim and s[counter+1] == 'M':
                    counter += 1
                    total += 900
                else:
                    total += 100
            elif thisone == 'L':
                total += 50
            elif thisone == 'X':
                if counter +1 < dim and s[counter+1] == 'C':
                    total += 90
                    counter += 1
                elif counter+1  < dim and s[counter+1] == 'L':
                    total += 40
                    counter += 1
                else:
                    total += 10
            elif thisone == 'V':
                    total += 5
            elif thisone == 'I':
                if counter +1 < dim and s[counter+1] == 'X':
                    total += 9
                    counter += 1
                elif counter +1 < dim and s[counter+1] == 'V':
                    total += 4
                    counter += 1
                else:
                    total += 1
            else:
                print 'invalid char = {0}'.format(thisone)
            counter += 1
        return total
