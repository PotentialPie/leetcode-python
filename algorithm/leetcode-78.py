class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        n = len(nums)
        out = []
        tmp = []

        def DFS(index):
            if index == n:
                out.append(tmp[:])
                return

            DFS(index + 1)

            tmp.append(nums[index])
            DFS(index + 1)
            tmp.remove(nums[index])

        DFS(0)

        return out
solution = Solution()
print(solution.subsets(nums = []))
print(solution.subsets(nums = [0]))
print(solution.subsets(nums = [0,1]))
print(solution.subsets(nums = [1,2,3]))
print(solution.subsets(nums = [3,2,1]))
