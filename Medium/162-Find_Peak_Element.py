# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

# Constraints:
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.

import random
import time

# SOLUTION
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low

# TEST
def is_peak(nums, i):
    # anything past the edges counts as -infinity
    if not isinstance(i, int) or not 0 <= i < len(nums):
        return False
    left = nums[i - 1] if i > 0 else float("-inf")
    right = nums[i + 1] if i < len(nums) - 1 else float("-inf")
    return nums[i] > left and nums[i] > right
 
 
class CountingList(list):
    # counts how many times the solution reads from the list
    def __init__(self, *args):
        super().__init__(*args)
        self.reads = 0
 
    def __getitem__(self, i):
        self.reads += 1
        return super().__getitem__(i)
 
 
def test_find_peak_element():
    sol = Solution()
 
    cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [5],                          # single element
        [1, 2],                       # peak at the end
        [2, 1],                       # peak at the start
        [1, 2, 3, 4, 5],              # strictly increasing
        [5, 4, 3, 2, 1],              # strictly decreasing
        [1, 3, 2, 4, 1],              # two peaks
        [3, 1, 2],                    # peaks at both edges
        [1, 5, 1, 5, 1, 5, 1],        # zigzag
        [-5, -3, -4],                 # negatives
        [-2**31, 2**31 - 1],          # constraint limits
        [2**31 - 1, -2**31],
    ]
    passed = 0
    for nums in cases:
        got = sol.findPeakElement(list(nums))
        if is_peak(nums, got):
            passed += 1
            print(f"PASS  {nums} -> {got}")
        else:
            print(f"FAIL  {nums} -> got {got}, which is not a peak")
 
    # 1000 random arrays with no equal neighbors
    rng = random.Random(42)
    random_ok = True
    for _ in range(1000):
        n = rng.randint(1, 1000)
        nums = [rng.randint(-1000, 1000)]
        while len(nums) < n:
            x = rng.randint(-1000, 1000)
            if x != nums[-1]:
                nums.append(x)
        got = sol.findPeakElement(list(nums))
        if not is_peak(nums, got):
            random_ok = False
            print(f"FAIL  random array of length {n} -> got {got}, not a peak")
            break
    passed += random_ok
    if random_ok:
        print("PASS  1000 random arrays")
 
    n = 100_000
    big_cases = [
        ("100k increasing", list(range(n))),
        ("100k decreasing", list(range(n, 0, -1))),
        ("100k mountain", list(range(n // 2)) + list(range(n // 2, 0, -1))),
    ]
    for name, nums in big_cases:
        counted = CountingList(nums)
        start = time.perf_counter()
        got = sol.findPeakElement(counted)
        ms = (time.perf_counter() - start) * 1000
        ok = is_peak(nums, got) and counted.reads <= 40
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name} -> {got}, "
              f"{counted.reads} reads, {ms:.2f} ms")
 
    total = len(cases) + 1 + len(big_cases)
    print(f"\n{passed}/{total} passed")
 
if __name__ == "__main__":
    test_find_peak_element()