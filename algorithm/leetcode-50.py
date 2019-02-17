class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                return power(x * x, n // 2)
            if n % 2 != 0:
                return x * power(x, n - 1)

        if n < 0:
            return round(1 / power(x, -n), 5)
        else:
            return round(power(x, n), 5)


solution = Solution()
print(solution.myPow(2.00000, 10))
print(solution.myPow(2.10000, 3))
print(solution.myPow(2.00000, -2))
print(solution.myPow(0, 2))
result_str = '.'*3
print(result_str)
result_str[1] = 'Q'
print(result_str)
