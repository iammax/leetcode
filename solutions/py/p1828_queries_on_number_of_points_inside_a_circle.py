class Solution:
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        sol = []
        for circle in queries:
            inside = 0
            x2, y2, radius = circle
            for point in points:
                x1, y1 = point
                dist = ((x1-x2)**2 + (y1-y2)**2)**.5
                if dist <= radius:
                    inside  += 1
            sol.append(inside)

        return(sol)        

