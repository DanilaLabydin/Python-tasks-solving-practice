class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        output = 0
        for i in range(len(s)):
            if i + 1 < len(s):
                if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                    output -= nums[s[i]]
                    continue

                if s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                    output -= nums[s[i]]
                    continue

                if s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                    output -= nums[s[i]]
                    continue

            output += nums[s[i]]
        return output


Test = Solution()
test1 = "III"  # 3
test2 = "LVIII"  # 58
test3 = "MCMXCIV"  # 1994


print(Test.romanToInt(test2))
