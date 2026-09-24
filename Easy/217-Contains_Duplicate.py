# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

import time

# SOLUTION
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

# TEST
def test_contains_duplicate():
    sol = Solution()

    cases = [
        # (input, expected)
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([7], False),
        ([0, 1], False),
        ([3, 3], True),
        ([1, 5, -1], False),
        ([-1, -1], True),
        ([10**9, -10**9, 10**9], True),
        ([5, 1, 2, 3, 4, 5], True),     # duplicate is first and last
    ]
    passed = 0
    for nums, expected in cases:
        got = sol.containsDuplicate(list(nums))
        if got == expected:
            passed += 1
            print(f"PASS  {nums} -> {got}")
        else:
            print(f"FAIL  {nums} -> got {got}, expected {expected}")

    big_cases = [
        ("100k distinct (the TLE case)", list(range(-50_000, 50_000)), False),
        ("100k, duplicate at the very end", list(range(100_000)) + [0], True),
    ]
    for name, nums, expected in big_cases:
        start = time.perf_counter()
        got = sol.containsDuplicate(nums)
        ms = (time.perf_counter() - start) * 1000
        ok = got == expected and ms < 1000
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name} -> {got} in {ms:.1f} ms")

    total = len(cases) + len(big_cases)
    print(f"\n{passed}/{total} passed")


if __name__ == "__main__":
    test_contains_duplicate()