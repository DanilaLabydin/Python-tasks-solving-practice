from typing import List


class Solution:
    def Jump(self, nums: List[int]) -> bool:
        count = 0

        if len(nums) == 1:
            return count

        # iterate over the array
        for i in range(len(nums)):
            # print(i)
            # count += 1
            # compute the len jump, the all next possible positions after the jump
            jump = nums[i]

            if jump == 0:
                return 0

            if i + jump >= len(nums):
                # count += 1
                return count

            indexes_next_positions = []
            max_jump = i

            for jump_len in range(1, jump + 1):
                indexes_next_positions.append(jump_len + i)

            # compute the potential next next p
            k = i
            for index_next_pos in indexes_next_positions:
                if index_next_pos >= len(nums):
                    count += 1
                    return count

                max_jump = max(max_jump, k + nums[index_next_pos])
                k += 1

                if i + max_jump >= len(nums):
                    count += 1
                    return count

            i = k
            # count +=1

        return count


Test = Solution()

array1 = [2, 3, 1, 1, 4]  # 2
array2 = [2, 3, 0, 1, 4]  # 2
array3 = [1, 2]  # 1
array4 = [0]  # 0
array5 = [1]  # 0
array6 = [2, 1]  # 1
array7 = [1, 3, 2]  # 2


print(Test.Jump(array3))
