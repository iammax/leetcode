class Solution(object):
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        out = []
        dim = len(arr)
        counter = 1
        prev = arr[0]
        while counter < dim:
            here = arr[counter]
            if counter == 1:
                mindist = here-prev
            gap = here-prev
            if gap == mindist:
                out.append([prev, here])
            elif gap < mindist:
                out = [[prev, here]]
                mindist = gap
            counter += 1
            prev = here
        return out
