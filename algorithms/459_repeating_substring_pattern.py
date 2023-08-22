class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = ""
        for i in range(len(s) // 2):
            pattern += s[i]

            splited_by_pattern = s.split(pattern)
            if not all(splited_by_pattern):
                return True

        return False
