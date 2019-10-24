# python3中， /是精确除法，//是向下取整除法，%是求模(向下取整求模)，四舍五入取整round, 向零取整int, 向下和向上取整函数math.floor, math.ceil

class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (2 << 31) - 1 if x > 0 else 2 << 31
        while y != 0:
            res = res * 10 + y % 10
            y //= 10
            if res > of:
                return 0
        return res if x > 0 else -res


print(Solution().reverse(123))
