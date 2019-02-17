class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        str2index_dict = {}
        for str_index in range(len(haystack)):
            if haystack[str_index] not in str2index_dict:
                str2index_dict[haystack[str_index]] = [1, str_index]
            else:
                str2index_dict[haystack[str_index]].append(str_index)
                # str2index_dict[haystack[str_index]][0] += 1

        if needle[0] in str2index_dict:
            head_index = str2index_dict[needle[0]][1]
            str2index_dict[needle[0]][0] += 1
        else:
            return -1

        last_index = head_index

        for needle_index in range(1, len(needle)):
            needle_str = needle[needle_index]
            if needle_str not in str2index_dict:
                #print('a')
                return -1
            elif str2index_dict[needle_str][0] == len(str2index_dict[needle_str]):
                #print('b')
                return -1
            elif str2index_dict[needle_str][str2index_dict[needle_str][0]] != last_index + 1:
                #print('c')
                return -1
            else:
                last_index = str2index_dict[needle_str][str2index_dict[needle_str][0]]
                str2index_dict[needle_str][0] += 1


        return head_index

solution = Solution()
# print(solution.strStr(haystack = "hello", needle = "ll"))
# print(solution.strStr(haystack = "aaaaa", needle = "bba"))
# print(solution.strStr(haystack = "aaaaa", needle = ""))
# print(solution.strStr(haystack = "aaaaa", needle = "aaa"))
print(solution.strStr(haystack = "aaa", needle = "aaa"))