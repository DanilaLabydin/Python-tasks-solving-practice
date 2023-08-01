from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_arr = nums.copy()

        for i in range(len(new_arr)):
            if i == 0:
                continue

            if new_arr[i] == new_arr[i - 1]:
                nums.remove(new_arr[i])

        return len(nums), nums


Test = Solution()
array1 = [1, 1]
array2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


print(Test.removeDuplicates(array1))
