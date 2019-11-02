class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


print(Solution().isPalindrome(121))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # 翻转x
        m, n = x, 0
        while m:
            n = n * 10 + m % 10
            print(n)
            m //= 10
            print(m)
        if n == x:
            return True


print(Solution().isPalindrome(10))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        m, n = x, 0
        while m > n:
            n = n * 10 + m % 10
            print(n)
            m //= 10
            print(m)
        if m == n or (n // 10) == m:
            return True
        else:
            return False


print(Solution().isPalindrome(0))
