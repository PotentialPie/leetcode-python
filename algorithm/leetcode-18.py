class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        ans = []
        sum_dict = {}

        nums.sort()
        #print(nums)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum = nums[i] + nums[j]
                if two_sum not in sum_dict:
                    sum_dict[two_sum] = [[i, j]]
                else:
                    # last_two_sum = sum_dict[two_sum][-1]
                    # if nums[last_two_sum[0]] == nums[i]:
                    #     continue
                    # else:
                    sum_dict[two_sum].append([i, j])

        #print(sum_dict)

        for i in range(len(nums) - 3):
            if i > 0 and i < len(nums) - 3 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    continue
                comp = target - nums[i] - nums[j]
                if comp not in sum_dict:
                    continue
                for two_sum in sum_dict[comp]:
                    if two_sum[0] > j:
                        if ans and ans[-1][-1] ==  nums[two_sum[1]] and ans[-1][-2] ==  nums[two_sum[0]] and ans[-1][-3] ==  nums[j] and ans[-1][-4] ==  nums[i]:
                            continue
                        ans.append([nums[i], nums[j], nums[two_sum[0]], nums[two_sum[1]]])

        return ans



solution = Solution()
print(solution.fourSum(nums = [1, 0, -1, 0, -2, 2], target = 0))

'''
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

sorted:[-2, -1, 0, 0, 1, 2]

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
