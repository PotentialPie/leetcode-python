#coding=utf-8
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        # if nums[left] == target:
        #     return left
        # elif nums[left] < target:
        #     return left + 1
        # else:
        #     if left == 0:
        #         return 0
        #     else:
        #         return left - 1
        # 这块好好再想想，当时为啥错
        if nums[left] >= target:
            return left
        else:
            return left + 1

solution = Solution()
print(solution.searchInsert([], 5))

print(solution.searchInsert([1], 5))
print(solution.searchInsert([5], 5))
print(solution.searchInsert([6], 5))

print(solution.searchInsert([1,5], 5))
print(solution.searchInsert([5,6], 5))
print(solution.searchInsert([1,4], 5))
print(solution.searchInsert([6,7], 5))
print(solution.searchInsert([1,6], 5))


print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1,3,5,6], 0))