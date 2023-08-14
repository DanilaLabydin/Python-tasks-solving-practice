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
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        output = 0
        for i in range(len(s)):
            if not i + 1 >= len(s):
                if nums.get(s[i] + s[i + 1]) is not None:
                    print(output)
                    output += nums.get(s[i] + s[i + 1])
                    i += 1
                    continue

            output += nums[s[i]]
            print(output)

        return output


Test = Solution()
test1 = "III"  # 3
test2 = "LVIII"  # 58
test3 = "MCMXCIV"  # 1994


print(Test.romanToInt(test3))
