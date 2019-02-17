class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        d = x//2 + 1
        peci = 1

        while abs(d * d - x) >= peci:
            d = (d + x / d) / 2.0;

        d = int(d)
        if d * d > x:
            d = d - 1
        return d

solution = Solution()
print(solution.mySqrt(0))
print(solution.mySqrt(8))
print(solution.mySqrt(2))
print(solution.mySqrt(1))
print(solution.mySqrt(10))
print(solution.mySqrt(9))
print(solution.mySqrt(100))
print(solution.mySqrt(101))
print(solution.mySqrt(120))
print(solution.mySqrt(121))
print(solution.mySqrt(4))