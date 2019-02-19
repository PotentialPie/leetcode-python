class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1,n+1)]
        C = []
        t = 1
        tmp = []

        for i in range(n):
            t = t * (i + 1)
            C.append(t)

        def DFS(nums, n):
            #print(nums, n)
            if not nums:
                return "".join(tmp)
            index = len(nums) - 1
            times = index - 1
            while index >= 0 and index*C[times] >= n:
                index = index - 1
            tmp.append(str(nums[index]))
            return DFS(nums[:index]+nums[index+1:], n-index*C[times])

        return DFS(nums, k)

solution = Solution()
#(solution.getPermutation(1,1))
print(solution.getPermutation(4,9))
#print(solution.getPermutation(3,3))

