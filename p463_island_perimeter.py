class Solution(object):
    def islandPerimeter(self, grid):
        dimx = len(grid)
        dimy = len(grid[0])
        landarea = 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]] #the four directions for you to look in at each space
        for x in range (dimx):
            for y in range (dimy):
                
                if grid[x][y] == 1: #only bother looking around if you are only land. otherwise, skip the space
                    for direction in directions: #calculate the position you are looking at
                        newx = x + direction[0] 
                        newy = y + direction[1]
                        if newx > -1 and newy > -1 and newx <= dimx-1 and newy <= dimy-1: #make sure you are looking somewhere that is on the grid. otherwise, it must be water
                            if grid[newx][newy] == 0: #if you see water from land, add 1 to perimeter. if this check fails, you are looking at land from land
                                landarea += 1
                        else: #if you see off the map from land, treat it as water, and add 1 to perimeter
                            landarea += 1       
                else:
                    pass
        return landarea
