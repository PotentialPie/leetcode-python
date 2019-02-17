#coding=utf-8
# print(-15//4)
# print(-15%4)
#
# print(15//4)
# print(15%4)
#
# print(-15//-4)
# print(-15%-4)
#
# print(15//-4)
# print(15%-4)
#
# print(-7//-3)
#
# print(3<<2)


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        is_neg = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            is_neg = True

        division = 0

        while abs_dividend >= abs_divisor:
            tmp_divide = 1
            tmp_sum = abs_divisor
            while tmp_sum + tmp_sum <= abs_dividend:
                tmp_sum = tmp_sum + tmp_sum
                tmp_divide = tmp_divide + tmp_divide
            division += tmp_divide
            abs_dividend -= tmp_sum

        # 边界一定要考虑的很清楚，不能马虎！！！
        # 这道题有毒吧，只考虑结果的边界

        if division > 2 ** 31 - 1 and is_neg:
            return -2 ** 31
        if division > 2 ** 31 - 1 and not is_neg:
            return 2 ** 31 - 1

        if is_neg:
            return -division
        else:
            return division

solution = Solution()
print(solution.divide(-15,-4))
print(solution.divide(15,-4))
print(solution.divide(15,4))
print(solution.divide(-15,4))
print(solution.divide(0,-4))
print(solution.divide(0,4))
print(solution.divide(1,-4))
print(solution.divide(1,4))
print(solution.divide(-1,-4))
print(solution.divide(-1,4))

