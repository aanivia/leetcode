"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution():
    def twoSum(self, nums, target):
        for i, m in enumerate(nums):
            j = i + 1
            while j < len(nums):
                if target == m + nums[j]:
                    return [i, j]
                else:
                    j += 1


print(Solution().twoSum([2, 7, 11, 15], 9))


class Solution2():
    def twoSum(self, nums, target):
        dict = {}
        for i, m in enumerate(nums):
            dict[m] = i
        for i, m in enumerate(nums):
            j = dict.get(target - m)
            if j is not None and j != i:
                return [i, j]


print(Solution2().twoSum([2, 7, 11, 15], 9))


class Solution3():
    def twoSum(self, nums, target):
        dict = {}
        for i, m in enumerate(nums):
            if dict.get(target - m) is not None:
                return [dict.get(target - m), i]
            dict[m] = i


print(Solution3().twoSum([2, 7, 11, 15], 9))
