from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs)
        output = ""

        for i in range(len(shortest_word)):
            for word in strs:
                if word[i] != shortest_word[i]:
                    return output

            output += word[i]
        return output


Test = Solution()

array1 = ["flower", "flow", "flight"]
array2 = ["dog", "racecar", "car"]

print(Test.longestCommonPrefix(array2))
