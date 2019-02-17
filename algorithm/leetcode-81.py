#coding=utf-8
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)

        left = 0
        right = len_nums - 1

        # 为空的边界，我是傻子吧～～～～～～～～～～～～～
        if not nums:
            return False

        while left <= right:
            if nums[left] > nums[right] and target > nums[right] and target < nums[left]:
                return False
            if nums[left] < nums[right] and (target > nums[right] or target < nums[left]):
                return False

            middle = (left + right) / 2

            if nums[left] <= nums[right]:
                if nums[middle] < target:
                    left = middle + 1
                    continue
                elif nums[middle] > target:
                    right = middle - 1
                    continue
                else:
                    return True

            if nums[middle] >= nums[left]:
                #print(1)
                #print(middle)
                if target > nums[middle]:
                    left = middle + 1
                    continue
                if target < nums[middle]:
                    if target >= nums[left]:
                        right = middle - 1
                        continue
                    if target <= nums[right]:
                        left = middle + 1
                        continue
                return True

            if nums[middle] <= nums[right]:
                #print(2)
                if target < nums[middle]:
                    right = middle - 1
                    continue
                if target > nums[middle]:
                    if target <= nums[right]:
                        left = middle + 1
                        continue
                    if target >= nums[left]:
                        right = right - 1
                        continue
                return True
        return False




solution = Solution()
print(solution.search(nums = [2], target = 2))
print(solution.search(nums = [2], target = 3))
print(solution.search(nums = [3,1,1], target = 0))
print(solution.search(nums = [2,2], target = 3))
print(solution.search(nums = [2,3,4,0,1,2], target = 3))
print(solution.search(nums = [2,2], target = 2))
print(solution.search(nums = [2,1,2], target = 2))
print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))
# print(solution.search(nums = [4,5,6,7,0,1,2], target = 3))
# print(solution.search(nums = [], target = 3))
# print(solution.search(nums = [3,1], target = 0))
print(solution.search(nums = [3,1], target = 1))
print(solution.search(nums = [2,5,6,0,0,1,2], target = 0))
print(solution.search(nums = [2,5,6,0,0,1,2], target = 3))
print(solution.search(nums = [1,3,1,1,1], target = 3))