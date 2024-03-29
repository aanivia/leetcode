"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class oldSolution:
    def removeDuplicates(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        return len(nums)


class Solution:
    def removeDuplicates(self, nums) -> int:
        # 定义两个指针p1，p2
        pre, cur = 0, 1
        while cur < len(nums):
            print(len(nums))
            if nums[pre] == nums[cur]:
                nums.pop(cur)
            else:
                pre, cur = pre + 1, cur + 1
        return len(nums)
