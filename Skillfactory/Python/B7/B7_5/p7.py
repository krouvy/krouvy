class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        result = 0

        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        if result > (2 ** 31) - 1:
            return 0
        return sign * result

def suka():
    print('сука')

def checkMain():
    print(__name__)


if __name__ == '__main__':
    checkMain()
    suka()

    num = Solution()
    x = -451
    print(x)
    print(num.reverse(x))

