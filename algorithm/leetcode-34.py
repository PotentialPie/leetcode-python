#coding=utf-8
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        index_one = -1
        index_two = -1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
                continue
            elif nums[middle] < target:
                left = middle + 1
                continue
            else:
                index_one, index_two = middle, middle
                while index_one - 1 >= 0 and nums[index_one] == nums[index_one - 1]:
                    index_one -= 1
                while index_two + 1 <= len(nums) - 1 and nums[index_two] == nums[index_two + 1]:
                    index_two += 1
                # 这个错误就不应该了，找到了答案要推出来呀
                break

        return [index_one, index_two]

solution = Solution()
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(solution.searchRange(nums = [8], target = 8))
print(solution.searchRange(nums = [8], target = 1))
print(solution.searchRange(nums = [], target = 3))
print(solution.searchRange(nums = [8, 8], target = 8))
print(solution.searchRange(nums = [8, 8], target = 3))
print(solution.searchRange(nums = [1, 8, 10], target = 8))
print(solution.searchRange(nums = [1, 8,8, 10], target = 8))
print(solution.searchRange(nums = [1, 8,8,8, 10], target = 8))
print(solution.searchRange(nums = [1, 2,3,4,5,8,8,8, 10], target = 8))
print(solution.searchRange(nums = [1, 2,8,8,9, 10,11,12], target = 8))
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))