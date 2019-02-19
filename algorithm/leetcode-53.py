class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_num = max(0, nums[0])
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = cur_sum + nums[i]
            largest_num = max(largest_num, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return largest_num
        # i = 0
        # j = 0
        # largest_num = nums[i]
        # tmp_largest = largest_num
        #
        # while j < len(nums):
        #     #print(i,j)
        #     if j == len(nums) - 1:
        #         while i <= j:
        #             tmp_largest = tmp_largest - nums[i]
        #             largest_num = max(largest_num, tmp_largest)
        #             i = i + 1
        #     if i > j:
        #         break
        #     while j < len(nums) - 1 and tmp_largest >= 0:
        #         j = j + 1
        #         tmp_largest = tmp_largest + nums[j]
        #         largest_num = max(largest_num, tmp_largest)
        #     while i < j and tmp_largest < 0:
        #         tmp_largest = tmp_largest - nums[i]
        #         largest_num = max(largest_num, tmp_largest)
        #         i = i + 1
        #     if i == j and i < len(nums)-1:
        #         i = i + 1
        #         j = j + 1
        #         tmp_largest = nums[i]
        #         largest_num = max(largest_num, tmp_largest)
        # return largest_num

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([-1,0,-2]))
print(solution.maxSubArray([-1]))
