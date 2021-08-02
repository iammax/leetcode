class Solution(object):
    def distributeCandies(self, candies, num_people):
        #won't be super fast, but the straightforward solution
        answer = [0]*num_people
        n = 1
        while candies > 0:
            index = (n-1)%num_people
            if n <= candies:
                answer[index] += n
                candies -= n
            else:
                answer[index] += candies
                candies = 0
            n += 1
        return answer
