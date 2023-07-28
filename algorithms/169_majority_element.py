from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nbs_dict = {}
        for num in nums:
            if num not in nbs_dict:
                nbs_dict[num] = 1
            else:
                nbs_dict[num] += 1

        return max(nbs_dict, key=nbs_dict.get)


Test = Solution()
array = [2, 2, 1, 1, 1, 2, 2]
array2 = [3, 3, 4]
print(Test.majorityElement(array))
