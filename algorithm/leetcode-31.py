#coding=utf-8
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        1 2 3 6
        1 2 6 3
        1 3 2 6
        1 3 6 2
        1 6 2 3 
        1 6 3 2
        2 1 3 6
        """

        len_nums = len(nums)

        nums_index = len_nums - 1

        while nums_index > 0:
            if nums[nums_index] <= nums[nums_index - 1]:
                nums_index = nums_index - 1
            else:
                swap_index = nums_index
                for i in range(len_nums - 1, nums_index - 1, -1):
                    if nums[i] > nums[nums_index - 1]:
                        swap_index = i
                        break
                tmp = nums[nums_index - 1]
                nums[nums_index - 1] = nums[swap_index]
                nums[swap_index] = tmp

                left = nums_index
                right = len_nums - 1
                while left < right:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                    left += 1
                    right -= 1
                break
        # 就是这个边界问题
        if nums_index == 0:
            left = 0
            right = len_nums - 1
            while left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1
        print(nums)

solution = Solution()
solution.nextPermutation([1,2,3])
solution.nextPermutation([1,4,2,5,4,3,2,1])
solution.nextPermutation([1])
solution.nextPermutation([1,1,5])
solution.nextPermutation([1,5,5])
solution.nextPermutation([1,5,1])
# 你看看，又是边界，题目都给了提示了还不处理，蠢猪
solution.nextPermutation([3,2,1])