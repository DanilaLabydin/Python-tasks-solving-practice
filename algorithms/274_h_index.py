from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # if len(citations) == 1 and citations[0] != 0:
        #     return 1

        max_h = 0
        for i in citations:
            selected_papers = [x for x in citations if x >= i]
            if len(selected_papers) == i:
                max_h = max(max_h, len(selected_papers))

        return max_h


Test = Solution()
array1 = [3, 0, 6, 1, 5]  # 3
array2 = [1, 3, 1]  # 1
array3 = [0]  # 0
array4 = [100]  # 1


print(Test.hIndex(array2))
