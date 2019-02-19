# coding=utf-8
class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


solution = Solution()
print(solution.permuteUnique([1,2,3]))
print(solution.permuteUnique([1,1,2]))
print(solution.permuteUnique([2,2,1,1]))

