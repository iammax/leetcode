class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longesttime = -1
        top_emp = -1
        prevtime = 0
        for log in logs:
            dur = log[1] - prevtime
            prevtime = log[1]
            if dur > longesttime:
                longesttime = dur
                top_emp = log[0]
            elif dur == longesttime:
                top_emp = min(log[0], top_emp)
        return top_emp
