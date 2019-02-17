#coding=utf-8
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        out = []
        sorted_intervals = sorted(intervals, key=lambda i: i.start)
        for i in range(len(sorted_intervals)):
            #print(i)
            if newInterval.start > sorted_intervals[i].end:
                out.append(sorted_intervals[i])
                # 这个神奇的边界也要考虑啊，看来还是得写单侧，把单个的情况放进去
                if i == len(sorted_intervals) - 1:
                    out.append(newInterval)
                    break
                continue
            if newInterval.end < sorted_intervals[i].start:
                out.append(newInterval)
                while i < len(sorted_intervals):
                    out.append(sorted_intervals[i])
                    # 粗心惹的祸，三个i+1没加
                    i = i + 1
                break
            newInterval.start = min(newInterval.start, sorted_intervals[i].start)
            # 这个边界要考虑好啊，首先得出现比len小，其次得在后面
            #while sorted_intervals[i].start <= newInterval.end and i < len(sorted_intervals):
            while i < len(sorted_intervals) and sorted_intervals[i].start <= newInterval.end  :
                newInterval.end = max(newInterval.end, sorted_intervals[i].end)
                # 粗心惹的祸，三个i+1没加
                i = i + 1
            out.append(newInterval)
            while i < len(sorted_intervals):
                out.append(sorted_intervals[i])
                # 粗心惹的祸，三个i+1没加
                i = i + 1
            break
        for i in out:
            print(i.start, i.end)
        print()
        return out

solution = Solution()
# input1 = [[1,3],[2,6],[8,10],[15,18]]
# std_input1 = [Interval(item[0], item[1]) for item in input1]
# solution.merge(std_input1)
#
# input2 = [[1,4],[4,5]]
# std_input2 = [Interval(item[0], item[1]) for item in input2]
# solution.merge(std_input2)


solution.insert([Interval(item[0], item[1]) for item in [[1,2],[3,5],[6,7],[8,10],[12,16]]], Interval(4, 8))
solution.insert([Interval(item[0], item[1]) for item in [[1,5]]], Interval(2, 3))
solution.insert([Interval(item[0], item[1]) for item in [[1,5]]], Interval(0, 0))
solution.insert([Interval(item[0], item[1]) for item in [[1,5]]], Interval(6, 8))