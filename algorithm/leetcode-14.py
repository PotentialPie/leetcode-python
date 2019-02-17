#coding=utf-8
# 这题能告诉我们什么呢？
# 1. python的break只能跳出一重循环，但是return可以立刻终止，可以利用这个特性
# 2. 利用一个额外的flag变量来判断是否再break外一层
# 3. 判断输入是不是空list
class Solution:
    def longestCommonPrefix(self, m):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     min_max_len = min([len(s) for s in strs])
    #     common_prefix = ''
    #     for prefix_index in range(min_max_len):
    #         for i in range(1, len(strs)):
    #             if strs[0][prefix_index] != strs[i][prefix_index]:
    #                 return common_prefix
    #         common_prefix = common_prefix + strs[0][prefix_index]
    #     return common_prefix

    #一个牛逼的解法
        if not m:
            return ''
        # since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        print(s1)
        s2 = max(m)
        print(s2)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]  # stop until hit the split index
        return s1

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))

print(7462266+149408+200000+285174+1790251)
