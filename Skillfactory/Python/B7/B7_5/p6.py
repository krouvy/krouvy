class Solution:
    def reverse(self, x: int) -> int:

        mod = 1
        razr = 1
        result = 0

        if x < 0:
            x *= -1
            mod = -1

        while x // razr > 9:
            razr *= 10

        while razr > 0:
            result += x % 10 * razr
            x //= 10
            razr //= 10

        if result > (2**31)-1:
            return 0
        return result * mod


print((2**31)-1 >= 1534236469)

num = Solution()
x = 15342
print(x)
print(num.reverse(x))
