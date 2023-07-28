from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        for num in nums_dict:
            if nums_dict[num] > 2:
                for _ in range(nums_dict[num] - 2):
                    nums.remove(num)

        return nums


Test = Solution()
array1 = [1, 1, 1, 2, 2, 3]
print(Test.removeDuplicates(array1))
