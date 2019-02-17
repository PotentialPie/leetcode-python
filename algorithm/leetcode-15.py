#coding=utf-8
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        nums.sort()
        results = []
        for i in range(len_nums - 2):
            j = i + 1
            k = len_nums - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    ## 这里，可能出现多个重复的情况，要++++++到底啊
                    ## 不过不能加到底的，要考虑上下限的
                    while nums[j] == nums[j - 1] and j < len_nums -1:
                        j = j + 1
                    while nums[k] == nums[k + 1] and k > i:
                        k = k - 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                else:
                    j = j + 1
        return results


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
