# coding=utf-8
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        used_dict = {}
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
                    # print(nums_index)
                    #print(result_list)
                    if nums[nums_index] in used_dict and index in used_dict[nums[nums_index]]:
                        #print(nums[nums_index], used_dict, index)
                        continue
                    if nums[nums_index] not in used_dict:
                        used_dict[nums[nums_index]] = [index]
                        #print('in', index, used_dict)
                    else:
                        used_dict[nums[nums_index]].append(index)
                        #print('in', index, used_dict)
                    used_flag[nums_index] = 1
                    cur_list.append(nums[nums_index])
                    dfs(index + 1, cur_list)
                    cur_list.remove(nums[nums_index])
                    # 我勒个乖乖，这种低级错误不能犯啊，回溯啊
                    used_flag[nums_index] = 0
                    # if len(used_dict[nums[nums_index]]) == 1:
                    #     used_dict.pop(nums[nums_index])
                    # else:
                    #     used_dict[nums[nums_index]].remove(index)
            for nums_index in range(len(nums)):
                if used_flag[nums_index] == 0:
                    if nums[nums_index] not in used_dict:
                        continue
                    if len(used_dict[nums[nums_index]]) == 1 and index in used_dict[nums[nums_index]]:
                        used_dict.pop(nums[nums_index])
                        #print('out', index, used_dict)
                    elif len(used_dict[nums[nums_index]]) > 1 and index in used_dict[nums[nums_index]]:
                        used_dict[nums[nums_index]].remove(index)
                        #print('out', index, used_dict)
        dfs(0, [])
        return result_list


solution = Solution()
#print(solution.permuteUnique([1,2,3]))
# print(solution.permuteUnique([1,1,2]))
print(solution.permuteUnique([2,2,1,1]))

