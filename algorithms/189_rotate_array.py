from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop(-1))


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move_part = nums[-k:]
        del nums[-k:]

        for num in move_part[::-1]:
            nums.insert(0, num)


Test = Solution2()
array = [1, 2, 3, 4, 5, 6, 7]
k = 3
Test.rotate(array, k)
print(array)
