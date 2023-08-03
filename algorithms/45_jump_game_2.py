from typing import List


class Solution:
    def Jump(self, nums: List[int]) -> bool:
        count = 0
        curr_index = 0

        while curr_index < len(nums):
            # print('fgdfg')
            value = nums[curr_index]
            # if value == 0:
            #     return count
            
            max_jump_size = 0
            for i in range(1, value + 1):
                if curr_index + i >= len(nums) - 1:
                    count += 1
                    return count

                next_index = nums[curr_index + i]
                next_value = nums[next_index]
                jump_size = next_value + next_index
                max_jump_size = max(max_jump_size, jump_size)
            
            curr_index = max_jump_size
            # print(curr_index)
            count += 1

        return count


Test = Solution()

array1 = [2, 3, 1, 1, 4]  # 2
array2 = [2, 3, 0, 1, 4] # 2
array3 = [1, 2] # 1
array4 = [0] # 0
array5 = [1]


print(Test.Jump(array3))
