class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out = []

        def DFS(index, left_s, comb):
            #print(index, left_s, comb)
            if index == 4 and left_s == '':
                out.append(comb[:])
                return
            if (4 - index) * 1 > len(left_s) or (4 - index) * 3 < len(left_s):
                return
            if index < 3:
                comb += left_s[:1] + '.'
                DFS(index + 1, left_s[1:], comb)
                comb = comb[:-2]
                if len(left_s) >= 2 and int(left_s[:2]) >= 10:
                    comb += left_s[:2] + '.'
                    DFS(index + 1, left_s[2:], comb)
                    comb = comb[:-3]
                if len(left_s) >= 3 and int(left_s[:3]) <= 255 and int(left_s[:3]) >= 100:
                    comb += left_s[:3] + '.'
                    DFS(index + 1, left_s[3:], comb)
                    comb = comb[:-4]
            if index == 3:
                comb += left_s[:1]
                DFS(index + 1, left_s[1:], comb)
                comb = comb[:-1]
                if len(left_s) >= 2 and int(left_s[:2]) >= 10:
                    comb += left_s[:2]
                    DFS(index + 1, left_s[2:], comb)
                    comb = comb[:-2]
                #print(comb)
                if len(left_s) >= 3 and int(left_s[:3]) <= 255 and int(left_s[:3]) >= 100:
                    comb += left_s[:3]
                    DFS(index + 1, left_s[3:], comb)
                    comb = comb[:-3]

        DFS(0, s, '')
        return out
a='123456'
print(a[:-3])
solution = Solution()
print(solution.restoreIpAddresses("0000"))
print(solution.restoreIpAddresses("010010"))
print(solution.restoreIpAddresses("521113"))
print(solution.restoreIpAddresses("52551113"))
print(solution.restoreIpAddresses("552551113"))
print(solution.restoreIpAddresses("2552551113"))
print(solution.restoreIpAddresses("25525511135"))
print(solution.restoreIpAddresses("1225525511135"))