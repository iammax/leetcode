class Solution(object):
    def calPoints(self, ops):
        input = ops
        newinput = []
        dim = len(input)
        input = input
        counter = 0
        while counter < dim:
    #	
            thischar = input[counter]
            if thischar == "C":
                del(newinput[-1])
                counter += 1
            else:
                newinput.append(thischar)
                counter += 1
        input = newinput
        total = 0
        counter = 0
        dim = len(input) 
        while counter < dim:
            thischar = input[counter]
            if thischar == "D":
                total += 2*input[counter-1]
                input[counter] = 2*input[counter-1]
                counter +=1
            elif thischar == "+":
                total += (input[counter-1] + input[counter-2])
                input[counter] = (input[counter-1] + input[counter-2])
                counter += 1
            else:
                input[counter] = int(thischar)
                total += int(thischar)
                counter += 1
        return total
