class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        nums.sort()
        closest_num = -99999
        for i in range(len_nums - 2):
            j = i + 1
            k = len_nums - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                temp_sum = nums[i] + nums[j] + nums[k]
                if abs(temp_sum - target) < abs(closest_num - target):
                    closest_num = temp_sum
                if temp_sum == target:
                    return target
                elif temp_sum > target:
                    k = k - 1
                else:
                    j = j + 1
        return closest_num

solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))
print(solution.threeSumClosest([-1, 2, 1, -4], 100))
print(solution.threeSumClosest([0, 0, 0, 0], -1))
print(solution.threeSumClosest([-1, 2, 1, -4], 0.3))
print(solution.threeSumClosest([-1, 2, 1, -4], 100))