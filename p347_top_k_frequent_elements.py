class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        for thing in nums:
            if thing not in d:
                d[thing] = 1
            else:
                d[thing] += 1
        outputs = []
        for key, value in sorted(d.iteritems(), key=lambda (keys,values): (values,keys)):
            outputs.append(key)
        return outputs[::-1][:k]
