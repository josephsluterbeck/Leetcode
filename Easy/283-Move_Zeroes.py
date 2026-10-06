# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1

import random
import time

# SOLUTION
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mark = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[mark], nums[r] = nums[r], nums[mark]
                mark += 1

# TEST
def reference(nums):
    non_zero = [x for x in nums if x != 0]
    return non_zero + [0] * (len(nums) - len(non_zero))
 
def test_move_zeroes():
    sol = Solution()
    cases = [
        # (input, expected)
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),   # LeetCode example 1
        ([0], [0]),                             # LeetCode example 2
        ([1], [1]),                             # single non-zero
        ([], []),                               # empty
        ([1, 2, 3], [1, 2, 3]),                 # no zeros (every swap is a self-swap)
        ([0, 0, 0], [0, 0, 0]),                 # all zeros
        ([0, 0, 1], [1, 0, 0]),                 # zeros first
        ([1, 0, 0], [1, 0, 0]),                 # already done
        ([4, 0, 5, 0, 0, 6], [4, 5, 6, 0, 0, 0]),
        ([-1, 0, -2, 0, 3], [-1, -2, 3, 0, 0]), # negatives aren't zero
        ([2, 1, 0, 2, 1], [2, 1, 2, 1, 0]),     # duplicates keep their order
        ([0, -0, 7], [7, 0, 0]),                # -0 == 0 in Python ints
    ]
 
    passed = 0
    total = len(cases)
 
    for i, (nums, expected) in enumerate(cases, 1):
        original = nums[:]
        work = nums[:]
        ret = sol.moveZeroes(work)
        ok = work == expected and ret is None
        if ok:
            passed += 1
            print(f"PASS {i}: {original} -> {work}")
        else:
            print(f"FAIL {i}: {original} -> got {work} (returned {ret!r}), expected {expected}")

    random.seed(283)
    big_cases = [
        ("10^5 random, ~30% zeros", [0 if random.random() < 0.3 else random.randint(-10**9, 10**9) for _ in range(10**5)]),
        ("10^6 random, ~50% zeros", [0 if random.random() < 0.5 else random.randint(1, 100) for _ in range(10**6)]),
        ("10^6 all zeros", [0] * 10**6),
        ("10^6 no zeros", list(range(1, 10**6 + 1))),
        ("10^6 zeros then ones", [0] * (5 * 10**5) + [1] * (5 * 10**5)),
    ]
 
    for name, nums in big_cases:
        total += 1
        expected = reference(nums)
        start = time.perf_counter()
        sol.moveZeroes(nums)
        elapsed = time.perf_counter() - start
        if nums == expected:
            passed += 1
            print(f"PASS big: {name} in {elapsed:.3f}s")
        else:
            print(f"FAIL big: {name} in {elapsed:.3f}s")
 
    print(f"\n{passed}/{total} passed")
 
if __name__ == "__main__":
    test_move_zeroes()