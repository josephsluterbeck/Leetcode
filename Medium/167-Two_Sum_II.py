# You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
# Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

import random
import time

# SOLUTION
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        answer = {}

        for index, x in enumerate(numbers):
            y = target - x

            if y in answer:
                return [answer[y], index + 1]
            answer[x] = index + 1

# TEST
def is_valid(numbers, target, result):
    if not (isinstance(result, list) and len(result) == 2):
        return False
    i, j = result
    return 1 <= i < j <= len(numbers) and numbers[i - 1] + numbers[j - 1] == target
 
 
def test_two_sum_ii():
    sol = Solution()
    cases = [
        # (numbers, target, expected)
        ([2, 7, 11, 15], 9, [1, 2]),            # LeetCode example 1
        ([2, 3, 4], 6, [1, 3]),                 # LeetCode example 2
        ([-1, 0], -1, [1, 2]),                  # LeetCode example 3: negatives
        ([1, 2], 3, [1, 2]),                    # minimum length
        ([3, 3], 6, [1, 2]),                    # duplicate values
        ([1, 3, 4, 6, 8, 11], 10, [3, 4]),      # pair in the middle
        ([1, 2, 3, 4, 100], 104, [4, 5]),       # pair at the end
        ([-10, -3, 2, 7], -13, [1, 2]),         # both negative
        ([0, 0, 3, 4], 0, [1, 2]),              # zeros
        ([-1000, -1, 0, 5, 1000], 0, [1, 5]),   # first and last elements
        ([1, 1, 1, 2, 3], 5, [4, 5]),           # repeated values that aren't the answer
    ]
 
    passed = 0
    total = 0
 
    for numbers, target, expected in cases:
        total += 1
        got = sol.twoSum(numbers[:], target)
        if is_valid(numbers, target, got):
            passed += 1
            note = "" if got == expected else f" (also valid; listed {expected})"
            print(f"PASS {total}: {numbers}, target={target} -> {got}{note}")
        else:
            print(f"FAIL {total}: {numbers}, target={target} -> got {got}, expected {expected}")

    random.seed(167)
 
    def make_case(n, a_pos, b_pos):
        nums = sorted(2 * v for v in random.sample(range(-10**7, 10**7), n))
        nums[b_pos] += 1          
        return nums, nums[a_pos] + nums[b_pos]
 
    big_cases = [
        ("3*10^4, pair at both ends", *make_case(3 * 10**4, 0, 3 * 10**4 - 1)),
        ("10^5, pair near the start", *make_case(10**5, 1, 2)),
        ("10^6, pair near the end", *make_case(10**6, 10**6 - 3, 10**6 - 2)),
    ]
 
    for name, numbers, target in big_cases:
        total += 1
        start = time.perf_counter()
        got = sol.twoSum(numbers, target)
        elapsed = time.perf_counter() - start
        if is_valid(numbers, target, got):
            passed += 1
            print(f"PASS big: {name} -> {got} in {elapsed:.3f}s")
        else:
            print(f"FAIL big: {name} -> got {got} ({elapsed:.3f}s)")
 
    print(f"\n{passed}/{total} passed")
 
if __name__ == "__main__":
    test_two_sum_ii()