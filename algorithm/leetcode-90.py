class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        out = []
        tmp = []
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1

        keys = list(nums_dict.keys())
        n = len(keys)

        def DFS(index):
            if index == n:
                out.append(tmp[:])
                return
            for i in range(nums_dict[keys[index]] + 1):
                for k in range(i):
                    tmp.append(keys[index])
                DFS(index + 1)
                for k in range(i):
                    tmp.remove(keys[index])

        DFS(0)
        return out

solution = Solution()
print(solution.subsetsWithDup([]))
print(solution.subsetsWithDup([1]))
print(solution.subsetsWithDup([1,1]))
print(solution.subsetsWithDup([1,2]))
print(solution.subsetsWithDup([1,2,3]))
print(solution.subsetsWithDup([1,2,2]))
print(solution.subsetsWithDup([1,2,2,1]))
print(solution.subsetsWithDup([2,2,2,2]))