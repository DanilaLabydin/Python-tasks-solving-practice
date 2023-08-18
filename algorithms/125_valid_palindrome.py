class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([letter for letter in s if letter.isalnum()])
        return clean_s.lower() == clean_s.lower()[::-1]


MySolution = Solution()

test1 = "A man, a plan, a canal: Panama"  # True
test2 = "race a car"  # False
test3 = " "  # True

print(MySolution.isPalindrome(test3))
