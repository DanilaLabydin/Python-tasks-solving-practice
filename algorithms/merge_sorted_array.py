from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_part = nums1[:m]
        right_part = nums2[:n]

        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if left_part[i] < right_part[j]:
                nums1[k] = left_part[i]
                i += 1
            else:
                nums1[k] = right_part[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = left_part[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = right_part[j]
            j += 1
            k += 1


class SolutionBest:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write_index = m - 1, n - 1, m + n - 1
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1
            write_index -= 1


Test = Solution()
# array1 = [1, 2, 3, 0, 0, 0]
# m = 3
# array2 = [2, 5, 6]
# n = 3

array1 = [0]
m = 0
array2 = [1]
n = 1

Test.merge(array1, m, array2, n)
print(array1)
