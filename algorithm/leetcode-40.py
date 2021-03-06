#coding=utf-8
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_list = []

        # 看看能不能加速咯
        count_dict ={}
        for item in candidates:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] += 1
        unique_keys = count_dict.keys()

        def dfs(index, left_sum, cur_result):
            if index == len(unique_keys) and left_sum != 0:
                return
            if index == len(unique_keys) and left_sum == 0:
                # 注意，如果不用这种方式[:]的话，append的是cur_result的引用，如果变化了，也会变化，所以要用副本
                result_list.append(cur_result[:])
                return
            # if left_sum > 0 and left_sum < candidates[index]:
            #     return
            if left_sum < 0:
                return

            for i in range(0, min((left_sum // unique_keys[index]) + 1, count_dict[unique_keys[index]]+1)):
                for dup in range(i):
                    cur_result.append(unique_keys[index])
                dfs(index + 1, left_sum - i * unique_keys[index], cur_result)
                for dup in range(i):
                    cur_result.remove(unique_keys[index])
        # 别忘了调用啊
        dfs(0, target, [])

        return result_list


solution = Solution()
print(solution.combinationSum(candidates = [5,3,7], target = 8))
print(solution.combinationSum(candidates = [1], target = 8))
print(solution.combinationSum(candidates = [8], target = 8))
print(solution.combinationSum(candidates = [2,3,5], target = 8))
print(solution.combinationSum(candidates = [2,3,6,7], target = 7))
print(solution.combinationSum(candidates = [2,3,5], target = 8))
print(solution.combinationSum(candidates = [10,1,2,7,6,1,5], target = 8))
print(solution.combinationSum(candidates = [2,5,2,1,2], target = 5))
