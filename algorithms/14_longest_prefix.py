from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs)
        common_prefix = ""

        for letter in shortest_word:
            print(letter)

            for word in strs:
                print(word, common_prefix, word.startswith(common_prefix))
                if not word.startswith(common_prefix):
                    return common_prefix

            common_prefix += letter

        return common_prefix


Test = Solution()

array1 = ["flower", "flow", "flight"]
array2 = ["dog", "racecar", "car"]

print(Test.longestCommonPrefix(array1))
