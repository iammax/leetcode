class Solution(object):
    def isRobotBounded(self, instructions):
        #vectors: 0 = north, 1 = east, 2 = south, 3 = west, mod 4
        vec_index = 0
        dx = 0
        dy = 0
        cat_steps = []
        
        numsteps = len(instructions)
        counter = 0
        L = 0
        R = 0
        G = 0
        for trial in range (0, 4):
            while counter < numsteps:
                dummy = False
                direct = instructions[counter]
                if direct == 'L':
                    L += 1
                    counter += 1
                elif direct == 'R':
                    R += 1
                    counter += 1
                else:
                    if L != R:
                        rotation = R-L
                        vec_index = (vec_index + rotation)%4
                    G = 0
                    while dummy == False and counter < numsteps: 
                        direct = instructions[counter]
                        if direct == 'G':
                            G += 1
                            counter += 1
                        else:
                            dummy = True
                    if vec_index == 0:
                        dy += G
                    elif vec_index == 1:
                        dx += G
                    elif vec_index == 2:
                        dy -= G
                    elif vec_index == 3:
                        dx -= G
                    else:
                        print "Vec_index has invallid value"
                    L = 0
                    R = 0
                    G = 0
            if dx == 0 and dy == 0:
                if trial != 2:
                    return True
            counter = 0
        return False
