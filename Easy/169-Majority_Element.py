# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# The input is generated such that a majority element will exist in the array.

import time

# SOLUTION
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        n = len(nums)

        for value in nums:
            count[value] = count.get(value, 0) + 1
        for num, frequency in count.items():
            if frequency > n / 2:
                return num
        return 0

# TEST
def test_majority_element():
    sol = Solution()
    cases = [
        # (nums, expected)
        ([3, 2, 3], 3),                    # Example 1
        ([2, 2, 1, 1, 1, 2, 2], 2),        # Example 2
        ([1], 1),                          # single element
        ([5, 5], 5),                       # two of the same
        ([1, 2, 1], 1),                    # odd length, minimum majority
        ([4, 4, 4, 4], 4),                 # all the same
        ([1, 2, 3, 3, 3], 3),              # majority at the end
        ([7, 7, 7, 1, 2], 7),              # majority at the start
        ([1, 9, 1, 9, 1], 1),              # alternating
        ([-1, -1, 2], -1),                 # negative numbers
        ([0, 0, 0, -5, 5], 0),             # zero as majority
        ([10**9, 10**9, -10**9], 10**9),   # max value
        ([-10**9, -10**9, 10**9], -10**9), # min value
        ([6, 5, 5], 5),                    # majority not first
        ([2, 1, 2, 1, 2, 1, 2], 2),        # n // 2 + 1 exactly
    ]

    passed = 0
    for nums, expected in cases:
        result = sol.majorityElement(nums[:])
        if result == expected:
            print(f"PASS: nums={nums} -> {result}")
            passed += 1
        else:
            print(f"FAIL: nums={nums} -> got {result}, expected {expected}")

    # Big-input cases (n = 5 * 10^4, the max)
    n = 5 * 10**4
    big_cases = [
        ("all same", [8] * n, 8),
        ("half + 1 majority", [1] * (n // 2 + 1) + list(range(2, n // 2 + 1)), 1),
        ("alternating with majority", [3 if i % 2 == 0 else -i for i in range(n - 1)] + [3], 3),
        ("all distinct except majority", [-7] * (n // 2 + 1) + list(range(n // 2 - 1)), -7),
    ]

    for name, nums, expected in big_cases:
        start = time.perf_counter()
        result = sol.majorityElement(nums)
        elapsed = (time.perf_counter() - start) * 1000
        if result == expected:
            print(f"PASS: {name} (n={len(nums)}) -> {result} in {elapsed:.2f} ms")
            passed += 1
        else:
            print(f"FAIL: {name} (n={len(nums)}) -> got {result}, expected {expected}")

    total = len(cases) + len(big_cases)
    print(f"\n{passed}/{total} passed")

if __name__ == "__main__":
    test_majority_element()