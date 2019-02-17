#coding=utf-8
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        nums.sort()
        result_list = []
        used_flag = [0 for i in range(len(nums))]

        def dfs(index, cur_list):
            #print(index, cur_list)
            if index == len(nums):
                result_list.append(cur_list[:])
                return
            for nums_index in range(len(nums)):
                if used_flag[nums_index] == 0:
                    #print(nums_index)
                    used_flag[nums_index] = 1
                    cur_list.append(nums[nums_index])
                    dfs(index + 1, cur_list)
                    cur_list.remove(nums[nums_index])
                    # 我勒个乖乖，这种低级错误不能犯啊，回溯啊
                    used_flag[nums_index] = 0

        dfs(0, [])
        return result_list


solution = Solution()
print(solution.permute([1,2,3]))
# print(solution.permute([1]))
# print(solution.permute([3,2,1]))

