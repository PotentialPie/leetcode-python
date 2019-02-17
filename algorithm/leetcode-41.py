class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        tmp_min_miss = 99999999999
        for i in range(len_nums):
            if nums[i] <= 0 or nums[i] > len_nums:
                continue
            #     if tmp_min_miss <= len_nums and nums[tmp_min_miss-1] == tmp_min_miss:
            #         tmp_min_miss = i + 1
            #     else:
            #         tmp_min_miss = min(i+1, tmp_min_miss)
            else:
                while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                    tmp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = tmp
                continue
                # if nums[i] == i + 1:
                #     continue
                # else:
                #     # if tmp_min_miss <= len_nums and nums[tmp_min_miss - 1] == tmp_min_miss:
                #     #     tmp_min_miss = i + 1
                #     # else:
                #     #     tmp_min_miss = min(i + 1, tmp_min_miss)
        for i in range(len_nums):
            if nums[i] != i + 1:
                return i+1
        return len_nums + 1

solution = Solution()
print(solution.firstMissingPositive([3,4,-1,1]))
print(solution.firstMissingPositive([1,1]))
print(solution.firstMissingPositive([0,-1,3,1]))