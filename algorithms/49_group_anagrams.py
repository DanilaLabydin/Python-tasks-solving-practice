from typing import List


class Solution:
    def get_letter_stat(self, word):
        output = {}
        for letter in word:
            if letter not in output:
                output[letter] = 1
            else:
                output[letter] += 1
        return output

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for word in strs:
            # print(word)
            letter_stat = self.get_letter_stat(word)
            # print(letter_stat)
            group = []
            for i in range(len(strs)):
                # print(self.get_letter_stat(strs[i]))
                if letter_stat == self.get_letter_stat(strs[i]):
                    # print('y')
                    group.append(strs[i])

            # print(group)
            output.append(group)
            # print(group)
            for word in group:
                strs.remove(word)
        # print(strs)
        for word in strs:
            output.append([word])
        return output


class Solution2:
    def get_letter_stat(self, word):
        output = {}
        for letter in word:
            if letter not in output:
                output[letter] = 1
            else:
                output[letter] += 1
        return output

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        for word in strs:
            # print(word)
            word_stat = self.get_letter_stat(word)
            # print(f'word: {word} - stat: {word_stat}')

            group = []
            for word2 in strs:
                word2_stat = self.get_letter_stat(word2)
                # print(f'word2: {word2} - stat: {word2_stat}')
                if word_stat == self.get_letter_stat(word2):
                    group.append(word2)
                    # strs.remove(word2)

            output.append(group)
            for j in group:
                strs.remove(j)
        if len(strs) != 0:
            output.append(strs)
        return output[::-1]


MySolution = Solution2()
print()

test1 = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat",
]  # [["bat"],["nat","tan"],["ate","eat","tea"]]
test2 = [""]  # [[""]]
test3 = ["a"]  # [["a"]]
test4 = ["stop", "pots", "reed", "", "tops", "deer", "opts", ""]

print(MySolution.groupAnagrams(test4))
