# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

import time

# SOLUTION
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for index, x in enumerate(nums):
            y = target - x

            if y in nums_map:
                return [nums_map[y], index]
            nums_map[x] = index

# TEST
def is_valid(nums, target, result):
    if not isinstance(result, list) or len(result) != 2:
        return False
    i, j = result
    return i != j and 0 <= i < len(nums) and 0 <= j < len(nums) and nums[i] + nums[j] == target
 
 
def test_two_sum():
    sol = Solution()
 
    cases = [
        # ((nums, target), expected)
        (([2, 7, 11, 15], 9), [0, 1]),           # LeetCode example 1
        (([3, 2, 4], 6), [1, 2]),                # example 2: must not pair 3 with itself
        (([3, 3], 6), [0, 1]),                   # example 3: duplicate values
        (([3, 1, 4, 6], 9), [0, 3]),             # pair far apart
        (([1, 5, 8, -2, 4], 2), [3, 4]),         # negative number
        (([-3, 4, 3, 90], 0), [0, 2]),           # target of zero
        (([-1, -2, -3, -4, -5], -8), [2, 4]),    # all negatives
        (([0, 4, 3, 0], 0), [0, 3]),             # zeros
        (([5, 75, 25], 100), [1, 2]),            # pair at the end
        (([10**9, -10**9, 7], 0), [0, 1]),       # extreme values
    ]
 
    passed = 0
    total = len(cases)
 
    for (nums, target), expected in cases:
        result = sol.twoSum(nums, target)
        ok = result == expected and is_valid(nums, target, result)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: twoSum({nums}, {target}) -> {result} (expected {expected})")
        if ok:
            passed += 1
 
    big_cases = [
        ("n = 10^4 (LeetCode max)", 10**4),
        ("n = 10^6 (stress)", 10**6),
    ]
 
    for label, n in big_cases:
        nums = list(range(n - 2)) + [10**9, 10**9 - 1]
        target = 2 * 10**9 - 1
        expected = [n - 2, n - 1]
 
        start = time.perf_counter()
        result = sol.twoSum(nums, target)
        elapsed = time.perf_counter() - start
 
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {label} -> {result} in {elapsed:.4f}s (expected {expected})")
        total += 1
        if ok:
            passed += 1
 
    print(f"\n{passed}/{total} passed")
 
if __name__ == "__main__":
    test_two_sum()