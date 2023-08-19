class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}

        for letter in ransomNote:
            if letter not in ransomNote_dict:
                ransomNote_dict[letter] = 1
            else:
                ransomNote_dict[letter] += 1

        for letter in magazine:
            if letter not in magazine_dict:
                magazine_dict[letter] = 1
            else:
                magazine_dict[letter] += 1

        for letter, count in ransomNote_dict.items():
            if magazine_dict.get(letter) is None or magazine_dict.get(letter) < count:
                return False

        return True


MySolution = Solution()

ransom1 = "a"  # False
magazine1 = "b"

ransom2 = "aa"  # False
magazine2 = "ab"

ransom3 = "aa"  # False
magazine3 = "aab"

print(MySolution.canConstruct(ransom3, magazine3))
