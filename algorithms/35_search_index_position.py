from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            num = nums[i]

            if num == target:
                return nums.index(num)

            if num > target:
                # print(i)
                nums.insert(i, target)
                return i

        return len(nums)


MySol = Solution()

nums1 = [1, 3, 5, 6]  # 2
t1 = 5
nums2 = [1, 3, 5, 6]  # 1
t2 = 2
nums3 = [1, 3, 5, 6]  # 4
t3 = 7

print(MySol.searchInsert(nums1, t1))
