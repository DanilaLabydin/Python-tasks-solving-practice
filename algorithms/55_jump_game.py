from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        for i in range(len(nums)):
            if nums[i] != 0:
                continue

            # iterate over prev values
            for k in range(1, len(nums[:i]) + 1):
                prev_index = i - k
                prev_num = nums[prev_index]
                if prev_num + prev_index >= len(nums) - 1 or prev_num + prev_index > i:
                    break

            else:
                return False

        return True


Test = Solution()

array1 = [2, 3, 1, 1, 4]  # True
array2 = [3, 2, 1, 0, 4]  # False
array3 = [0, 1]  # False
array4 = [0]  # True
array5 = [2, 0]  # True
array6 = [2, 0, 0]  # True
array7 = [1, 1, 0, 1]  # False
array8 = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]  # True

print(Test.canJump(array1))
