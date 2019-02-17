class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        # reachable_flag = [0 for i in range(len(nums))]
        # reachable_flag[0] = 1
        # for i in range(len(nums)):
        #     #print(i,nums[i])
        #     if reachable_flag[i] == 1:
        #         for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
        #             reachable_flag[j] = 1
        #         #print(reachable_flag)
        # if reachable_flag[len(nums) - 1] == 0:
        #     return False
        # else:
        #     return True

        max_reachable, last_index = 0, len(nums)-1
        max_reachable = nums[0]

        i = 0
        while i <= max_reachable and max_reachable < last_index:
            max_reachable = max(max_reachable, nums[i] + i)
            i = i + 1

        return max_reachable >=last_index





solution = Solution()
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,2,1,0,4]))
print(solution.canJump([]))