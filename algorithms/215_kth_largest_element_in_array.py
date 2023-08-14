from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_elements = []
        for _ in range(k):
            if len(nums) == 0:
                return max_elements[-1]

            local_max = max(nums)
            local_max_freq = nums.count(local_max)

            for _ in range(local_max_freq):
                nums.remove(local_max)
                max_elements.append(local_max)

                if len(max_elements) == k:
                    return max_elements[-1]

        # for i in range(k):
        #     if len(nums) == 0:
        #         return max_elements[k-1]

        #     local_max = nums[0]
        #     for j in range(1, len(nums)):
        #         local_max = max(local_max, nums[j])

        #     local_max_freq = nums.count(local_max)

        #     for _ in range(local_max_freq):
        #         nums.remove(local_max)
        #         max_elements.append(local_max)

        #         if len(max_elements) >= k:
        #             return max_elements[-1]


array1 = [3, 2, 1, 5, 6, 4]  # 5
k1 = 2

array2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]  # 4
k2 = 4

array3 = [-1, -1]  # -1
k3 = 2

Test = Solution()
print(Test.findKthLargest(array1, k1))
