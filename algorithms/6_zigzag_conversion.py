class Solution:
    def get_encoded_lists(self, s, numRows):
        encoded_lists = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i == len(s):
                    return encoded_lists

                encoded_lists[j].append(s[i])
                i += 1

            for j in range(numRows - 2, 0, -1):
                if i == len(s):
                    return encoded_lists

                encoded_lists[j].append(s[i])
                i += 1

        return encoded_lists

    def convert(self, s: str, numRows: int) -> str:
        encoded_lists = self.get_encoded_lists(s, numRows)
        output = ""
        for list_ in encoded_lists:
            output += "".join(list_)

        return output


MySolution = Solution()
test1 = "PAYPALISHIRING"  # PAHNAPLSIIGYIR
num1 = 3
test2 = "A"  # A
num2 = 1

print(MySolution.convert(test1, num1))
