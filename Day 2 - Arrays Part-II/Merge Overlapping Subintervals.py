# Coded by Shalu Ambasta :)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans = []

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if len(ans) == 0:
                ans.append(intervals[i])

            if start <= ans[-1][1]:
                nend = max(end, ans[-1][1])
                nstart = ans[-1][0]
                ans.pop(-1)
                ans.append([nstart, nend])
            else:
                ans.append(intervals[i])

        return ans
        