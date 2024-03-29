class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i, m in enumerate(s):
            if dict.get(s[i]) <= dict.get(s[max(i - 1, 0)]):
                sum = sum + dict.get(m)
            else:
                sum = sum + dict.get(m) - 2 * dict.get(s[i - 1])
        return sum


print(Solution().romanToInt("LVIII"))
