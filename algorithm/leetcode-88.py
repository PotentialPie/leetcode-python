class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        while j <= n - 1:
            while nums2[j] > nums1[i] and i <= m - 1:
                i = i + 1
            nums1.insert(i, nums2[j])
            nums1.pop()
            m = m + 1
            j = j + 1
        return nums1

solution = Solution()
print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6],n = 3))
