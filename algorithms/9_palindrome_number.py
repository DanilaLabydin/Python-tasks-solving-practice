class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp_num = x
        reversed_num = 0

        while temp_num != 0:
            reversed_num = (reversed_num * 10) + (temp_num % 10)
            temp_num //= 10

        # print(reversed_num)
        return reversed_num == x


MySol = Solution()

test1 = 121
test2 = -121
test3 = 0

print(MySol.isPalindrome(test3))
