s = "11111222223"
k = 3


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = list(map(int, s))

            sLen = len(s)
            kolOp = sLen // k
            if int(sLen % k) > 0:
                kolOp += 1

            fromIndex = 0
            toIndex = k
            strArray = []

            for i in range(0, kolOp):
                sNumber = sum(s[fromIndex:toIndex])
                strArray.append(str(sNumber))
                fromIndex += k
                toIndex += k
            s = ''.join(strArray)
        return s


exm = Solution()
print(exm.digitSum(s, k))
