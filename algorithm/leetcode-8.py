#coding=utf-8
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        #print(str)
        str_no_w = str.strip()
        # 输入的边界啊，边界啊，边界啊，边界啊，边界啊！！！！！！！！！！！！！！！！
        if not str_no_w:
            return 0
        #print(str_no_w)
        i = 0
        neg = False
        if str_no_w[i] == '+':
            i = i + 1
        elif str_no_w[i] == '-':
            i = i + 1
            neg = True
        elif not str_no_w[i].isdigit():
            return 0
        value = 0
        for left_index in range(i, len(str_no_w)):
            if str_no_w[left_index].isdigit():
                value = value * 10 + int(str_no_w[left_index])
            # Input
            # "  -0012a42"
            else:
                break
        if neg:
            value = -value

        if value > INT_MAX:
            value = INT_MAX
        if value < INT_MIN:
            value = INT_MIN

        return value

# TODO
# 正则表达式的实现法





solution = Solution()
print(solution.myAtoi('  -0012a42'))
print(solution.myAtoi('   -42'))
print(solution.myAtoi('4193 with words'))
print(solution.myAtoi('words and 987'))
print(solution.myAtoi('-91283472332'))