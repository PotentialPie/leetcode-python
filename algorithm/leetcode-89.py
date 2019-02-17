class Solution(object):
    def grayCode(self, n):

        out = [0]

        for i in range(n):
            out = out + [k + 2 ** i for k in reversed(out)]
            print(out)

        return out

solution = Solution()
print(solution.grayCode(3))