class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """


        C = []
        t = 1


        for i in range(n):
            t = t * (i + 1)
            C.append(t)

        is_used = [0 for i in range(n)]
        result_out = []

        def DFS(index, left_num):

            if index == 1:
                for i in range(len(is_used) - 1, -1, -1):
                    if is_used[i] == 0:
                        result_out.append(str(i + 1))
                        return ''.join(result_out)
            tmp_index = index
            for i in range(len(is_used) - 1, -1, -1):
                if is_used[i] == 0 and (tmp_index - 1) * C[index - 2] < left_num:
                    is_used[i] = 1
                    result_out.append(str(i + 1))
                    #print(tmp_index, index, left_num, i + 1)
                    return DFS(index - 1, left_num - (tmp_index - 1) * C[index - 2])
                elif is_used[i] == 0:
                    tmp_index = tmp_index - 1
                    continue
                else:
                    continue

        return DFS(n, k)

solution = Solution()
print(solution.getPermutation(1,1))
print(solution.getPermutation(4,9))
print(solution.getPermutation(3,3))

