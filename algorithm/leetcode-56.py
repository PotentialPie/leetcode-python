#coding=utf-8
#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# 总结三个问题：
# 看下面的代码即可
# a = [1,2,3,4]
# for item in a:
#     print(item)
#     if item == 1:
#         a.remove(item)
#
#
# c = [1,2,3]
# b = c
# b[0]=3
# print(c,b)

# 第三个问题：break和continue都只针对当前的循环

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        merged_list = []
        merged_list.append(intervals[0])

        for i in range(1, len(intervals)):
            tmp_intervals = intervals[i]
            copy_list = merged_list[:]
            for known_intervals in merged_list:
                if known_intervals.start > tmp_intervals.end or known_intervals.end < tmp_intervals.start:
                    continue
                tmp_intervals.start = min(known_intervals.start, tmp_intervals.start)
                tmp_intervals.end = max(known_intervals.end, tmp_intervals.end)
                copy_list.remove(known_intervals)
            copy_list.append(tmp_intervals)
            merged_list = copy_list
            for merged_interval in merged_list:
                print(merged_interval.start, merged_interval.end)
            print()
        return merged_list

        # TODO
        # 一个更加高效的解决问题的办法，对s和e全部进行排序后，再操作
        # def merge(self, intervals):
        #     out = []
        #     for i in sorted(intervals, key=lambda i: i.start):
        #         if out and i.start <= out[-1].end:
        #             out[-1].end = max(out[-1].end, i.end)
        #         else:
        #             out += i,
        #     return out


solution = Solution()
# input1 = [[1,3],[2,6],[8,10],[15,18]]
# std_input1 = [Interval(item[0], item[1]) for item in input1]
# solution.merge(std_input1)
#
# input2 = [[1,4],[4,5]]
# std_input2 = [Interval(item[0], item[1]) for item in input2]
# solution.merge(std_input2)

input3 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
std_input3 = [Interval(item[0], item[1]) for item in input3]
solution.merge(std_input3)

print(solution.merge([]))

