class Solution(object):
    def sampleStats(self, count):
        total = 0
        counter = 0
        dim = len(count)
        most_id = 0
        most_count = 0
        minimum = -1
        maximum = -1
        population = 0
        while counter < dim:
            here = count[counter]
            if minimum == -1 and here > 0:
                minimum = counter
            if here > 0:
                maximum = counter
            total += counter*here
            if here > most_count:
                most_count = here
                most_id = counter
            counter += 1
            population += here
        if population %2 == 0:
            med_loc_1 = population/2
            med_loc_2 = med_loc_1 -1
        else:
            med_loc_1 = population/2
            med_loc_2 = population/2
        counter = 0
        used = 0
        med_id_1 = -1
        while counter < dim:
            here = count[counter]
            used += here
            if used < med_loc_1:
                pass
            elif used == med_loc_1:
                med_id_1 = counter
            elif used > med_loc_1:
                if med_id_1 == -1:
                    med = counter
                else:
                    med_id_2 = counter
                    med = .5*(med_id_1 + med_id_2)
                counter = dim
            counter += 1
        return [float(minimum), float(maximum), float(total)/population, med, most_id]
