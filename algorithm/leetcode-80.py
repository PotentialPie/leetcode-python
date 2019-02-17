class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        total_len = 1
        tmp_num = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if tmp_num < 2:
                    nums[total_len] = nums[i]
                    tmp_num += 1
                    total_len += 1
                elif tmp_num == 2:
                    continue
            else:
                nums[total_len] = nums[i]
                tmp_num = 1
                total_len += 1
        #print(nums[:total_len])
        return total_len

solution = Solution()
print(solution.removeDuplicates([]))
print(solution.removeDuplicates([1]))
print(solution.removeDuplicates([1,1]))
print(solution.removeDuplicates([1,2]))
print(solution.removeDuplicates([1,1,1]))
print(solution.removeDuplicates([1,1,1,2,2,3]))
print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(solution.removeDuplicates([0,0,0,0,0,0,1,1,1,1,1,1,1,2,3,3]))