class Solution(object):
    def findRestaurant(self, list1, list2):
        best = 'a'
        bestone = []
        for restaurant in list1:
            if restaurant in list2:
                pref = list1.index(restaurant) + list2.index(restaurant)
                if best == 'a':
                    best = pref
                    bestone = [restaurant]
                else:
                    if pref <= best:
                        best = pref
                        bestone.append(restaurant)
        return bestone
