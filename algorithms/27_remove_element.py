from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for _ in range(count):
            nums.remove(val)
        return len(nums), nums


Test = Solution()
array = [3, 2, 2, 3]
val = 3
Test.removeElement(array, val)
print(array)
