# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 
# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

import time

# SOLUTION
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        seen = set()

        for value in arr:
            count[value] = count.get(value, 0) + 1
        for num, frequency in count.items():
            if frequency in seen:
                return False
            seen.add(frequency)
        return True

# TEST
def test_unique_occurrences():
    sol = Solution()

    cases = [
        # (arr, expected)
        ([1, 2, 2, 1, 1, 3], True),                       # LeetCode example 1: counts 3, 2, 1
        ([1, 2], False),                                  # LeetCode example 2: counts 1, 1
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),       # LeetCode example 3: counts 3, 2, 4, 1
        ([5], True),                                      # single element
        ([7, 7, 7, 7], True),                             # one distinct value
        ([1, 1, 2, 2], False),                            # counts 2, 2
        ([1, 2, 2, 3, 3, 3], True),                       # counts 1, 2, 3
        ([1, 2, 2, 3, 3, 3, 4, 4, 4], False),             # counts 1, 2, 3, 3 (clash at the end)
        ([-1000, 1000, 1000], True),                      # constraint limits
        ([3, 1, 3, 2, 3, 2], True),                       # unsorted input, counts 3, 1, 2
    ]
    passed = 0
    for arr, expected in cases:
        got = sol.uniqueOccurrences(list(arr))
        if got == expected:
            passed += 1
            print(f"PASS  {arr} -> {got}")
        else:
            print(f"FAIL  {arr} -> got {got}, expected {expected}")

    unique_big = [k for k in range(1, 448) for _ in range(k)]
    clash_big = list(range(100_000))
    big_cases = [
        (f"{len(unique_big):,} items, all counts different", unique_big, True),
        (f"{len(clash_big):,} items, all counts equal", clash_big, False),
    ]
    for name, arr, expected in big_cases:
        start = time.perf_counter()
        got = sol.uniqueOccurrences(arr)
        ms = (time.perf_counter() - start) * 1000
        ok = got == expected and ms < 1000
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name} -> {got} in {ms:.1f} ms")

    total = len(cases) + len(big_cases)
    print(f"\n{passed}/{total} passed")

if __name__ == "__main__":
    test_unique_occurrences()