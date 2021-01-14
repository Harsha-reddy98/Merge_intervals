class Solution(object):
    def merge(self, intervals):

        intervals.sort(key = lambda s:s[0]) #sorting intervals based on the 1st term using lambda

        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][0] = min(intervals[i-1][0],intervals[i][0])  #minimum of both interval's first index
                intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])  #maximum of both intervals's second index

                interval.pop(i)     # removing ith index as we are combining both intervals

            else:
                i += 1
        return intervals 


        