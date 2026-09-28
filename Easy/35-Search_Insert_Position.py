# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4

import time

# SOLUTION
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)

# TEST
def test_search_insert():
    sol = Solution()
 
    cases = [
        # (nums, target, expected)
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),            # insert before everything
        ([1, 3, 5, 6], 1, 0),            # found at first index
        ([1, 3, 5, 6], 6, 3),            # found at last index
        ([1, 3, 5, 6], 4, 2),            # insert in the middle
        ([2, 4, 6, 8, 10], 8, 3),
        ([5], 5, 0),
        ([5], 2, 0),
        ([5], 9, 1),
        ([-10, -3, 0, 4], -3, 1),
        ([-10, -3, 0, 4], -5, 1),
        ([-10, -3, 0, 4], -11, 0),
        ([-10**4, 0, 10**4], 10**4, 2),  # constraint limits
        ([], 3, 0),                      # empty list
    ]
    passed = 0
    for nums, target, expected in cases:
        got = sol.searchInsert(list(nums), target)
        if got == expected:
            passed += 1
            print(f"PASS  {nums}, {target} -> {got}")
        else:
            print(f"FAIL  {nums}, {target} -> got {got}, expected {expected}")
 
    nums = [1, 3, 5, 6]
    sol.searchInsert(nums, 2)
    ok = nums == [1, 3, 5, 6]
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  input not modified -> list is now {nums}")
 
    big = list(range(0, 200_000, 2))     # 100k sorted even numbers
    big_cases = [
        ("100k, target missing in middle", big, 100_001, 50_001),
        ("100k, target found at the end", big, 199_998, 99_999),
        ("100k, target past the end", big, 500_000, 100_000),
    ]
    for name, nums, target, expected in big_cases:
        start = time.perf_counter()
        got = sol.searchInsert(list(nums), target)
        ms = (time.perf_counter() - start) * 1000
        ok = got == expected and ms < 1000
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name} -> {got} in {ms:.1f} ms")
 
    total = len(cases) + 1 + len(big_cases)
    print(f"\n{passed}/{total} passed")
 
if __name__ == "__main__":
    test_search_insert()