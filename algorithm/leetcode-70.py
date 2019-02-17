class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        df = [0 for i in range(n)]
        df[0], df[1] = 1, 2

        for i in range(2, n):
            df[i] = df[i - 1] + df[i - 2]

        return df[n - 1]

solution = Solution()
print(solution.climbStairs(0))
print(solution.climbStairs(1))
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(4))