class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0 or k > n:
            return []
        out = []
        # used_flag = [0 for i in range(n)]
        tmp = []

        def DFS(index, start):
            if index == k:
                out.append(tmp[:])
            if k - index > n - start:
                return
            for i in range(start, n):
                tmp.append(i + 1)
                DFS(index + 1, i + 1)
                tmp.remove(i + 1)

        DFS(0, 0)
        return out


solution = Solution()
print(solution.combine(0,1))
print(solution.combine(1,0))
print(solution.combine(1,1))
print(solution.combine(0,0))
print(solution.combine(3,4))
print(solution.combine(4,1))
print(solution.combine(4,3))
print(solution.combine(4,4))
