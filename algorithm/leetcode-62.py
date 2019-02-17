class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def comnination(d, k):
            if d == 0 or k == 0:
                return 1
            base = 1
            for i in range(1, k + 1):
                base = base * i
            top_base = 1
            for i in range(d, d - k, -1):
                top_base = top_base * i
            return top_base / base

        d = m - 1 + n - 1
        k = min(m, n) - 1
        return comnination(d, k)

solution = Solution()
print(solution.uniquePaths(3,2))
print(solution.uniquePaths(2,2))
print(solution.uniquePaths(4,3))
print(solution.uniquePaths(1,1))
print(solution.uniquePaths(6,1))
print(solution.uniquePaths(1,6))
print(solution.uniquePaths(7,6))