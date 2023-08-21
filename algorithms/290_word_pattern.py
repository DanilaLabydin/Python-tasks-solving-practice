class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        s_dict = {}

        for letter in pattern:
            if letter not in pattern_dict:
                pattern_dict[letter] = 1
            else:
                pattern_dict[letter] += 1

        for word in s.split():
            first_letter = word[0]
            if first_letter not in s_dict:
                s_dict[first_letter] = 1
            else:
                s_dict[first_letter] += 1

        return list(pattern_dict.values()) == list(s_dict.values())


MySol = Solution()

pat1 = "abba"  # True
s1 = "dog cat cat dog"
pat2 = "abba"  # False
s2 = "dog cat cat fish"
pat3 = "aaaa"  # False
s3 = "dog cat cat dog"

print(MySol.wordPattern(pat3, s3))
