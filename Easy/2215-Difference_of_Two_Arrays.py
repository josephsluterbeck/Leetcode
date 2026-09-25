# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

import time

# SOLUTION
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[], []]
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for num in nums1_set:
            if num not in nums2_set:
                answer[0].append(num)
        for num in nums2_set:
            if num not in nums1_set:
                answer[1].append(num)
        return answer

# TEST
def normalize(answer):
    return [sorted(answer[0]), sorted(answer[1])]

def test_find_difference():
    sol = Solution()

    cases = [
        # (nums1, nums2, expected)
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),              # LeetCode example 1
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),              # LeetCode example 2
        ([1, 2, 3], [1, 2, 3], [[], []]),                     # identical
        ([1, 2, 3], [4, 5, 6], [[1, 2, 3], [4, 5, 6]]),       # nothing shared
        ([5, 5, 5], [5], [[], []]),                           # duplicates only
        ([7, 7, 8, 8], [9, 9], [[7, 8], [9]]),                # each distinct value listed once
        ([-1, 0, 1], [0], [[-1, 1], []]),                     # negatives and zero
        ([-1000, 1000], [1000, -999], [[-1000], [-999]]),     # constraint limits
        ([1], [2], [[1], [2]]),                               # single elements
    ]
    passed = 0
    for nums1, nums2, expected in cases:
        got = normalize(sol.findDifference(list(nums1), list(nums2)))
        if got == normalize(expected):
            passed += 1
            print(f"PASS  {nums1}, {nums2} -> {got}")
        else:
            print(f"FAIL  {nums1}, {nums2} -> got {got}, expected {expected}")

    a, b = [3, 1, 3], [1, 2]
    sol.findDifference(a, b)
    ok = a == [3, 1, 3] and b == [1, 2]
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  inputs left unchanged")

    big1 = list(range(0, 200_000))         
    big2 = list(range(100_000, 300_000))    
    start = time.perf_counter()
    got = sol.findDifference(big1, big2)
    ms = (time.perf_counter() - start) * 1000
    ok = (sorted(got[0]) == list(range(0, 100_000))
          and sorted(got[1]) == list(range(200_000, 300_000))
          and ms < 1000)
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  200k vs 200k (half shared) in {ms:.1f} ms")

    total = len(cases) + 2
    print(f"\n{passed}/{total} passed")


if __name__ == "__main__":
    test_find_difference()