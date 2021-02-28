from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    max_sum = 0
    for i in range(k):
        sub_list = nums[0 : i + 1]
        next_sum = sum(sub_list)
        if next_sum > max_sum:
            max_sum = next_sum
    return max_sum


a = [1, 3, -1, -3, 5, 3, 6, 7]
print(find_maximal_subarray_sum(a, 3))  # returns 18 (= 5 + 6 + 7)
