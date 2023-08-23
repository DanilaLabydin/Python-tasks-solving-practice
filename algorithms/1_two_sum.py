from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]


MySol = Solution()

nums1 = [2, 7, 11, 15]  # [0,1]
t1 = 9
nums2 = [3, 2, 4]  # [1,2]
t2 = 6
nums3 = [3, 3]  # [0, 1]
t3 = 6
nums4 = [-3, 4, 3, 90]  # [0, 2]
t4 = 0

print(MySol.twoSum(nums4, t4))
