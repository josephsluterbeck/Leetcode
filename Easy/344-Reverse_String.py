# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.

import time

# SOLUTION
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# TEST
def test_reverse_string():
    sol = Solution()
    cases = [
        # (s, expected)
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),            # Example 1
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),  # Example 2
        (["a"], ["a"]),                                                    # single char
        (["a", "b"], ["b", "a"]),                                          # two chars
        (["a", "b", "c"], ["c", "b", "a"]),                                # odd length
        (["a", "b", "c", "d"], ["d", "c", "b", "a"]),                      # even length
        (["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e", "c", "a", "r"]),  # palindrome
        (["x", "x", "x"], ["x", "x", "x"]),                                # all same
        ([" ", "a", " "], [" ", "a", " "]),                                # spaces
        (["1", "2", "3"], ["3", "2", "1"]),                                # digits
        (["!", "@", "#", "~"], ["~", "#", "@", "!"]),                      # symbols
        (["A", "b", "C", "d"], ["d", "C", "b", "A"]),                      # mixed case
    ]

    passed = 0
    for s, expected in cases:
        original = s[:]
        ref = s
        result = sol.reverseString(s)
        if s == expected and s is ref and result is None:
            print(f"PASS: s={original} -> {s}")
            passed += 1
        else:
            print(f"FAIL: s={original} -> got {s}, expected {expected} "
                  f"(in-place={s is ref}, returned={result})")

    # Big-input cases (n = 10^5, the max)
    n = 10**5
    printable = [chr(c) for c in range(32, 127)]
    big_cases = [
        ("all same", ["z"] * n),
        ("cycling printable ascii", [printable[i % len(printable)] for i in range(n)]),
        ("odd length max - 1", [printable[i % len(printable)] for i in range(n - 1)]),
    ]

    for name, s in big_cases:
        expected = s[::-1]
        ref = s
        start = time.perf_counter()
        result = sol.reverseString(s)
        elapsed = (time.perf_counter() - start) * 1000
        if s == expected and s is ref and result is None:
            print(f"PASS: {name} (n={len(s)}) in {elapsed:.2f} ms")
            passed += 1
        else:
            print(f"FAIL: {name} (n={len(s)})")

    total = len(cases) + len(big_cases)
    print(f"\n{passed}/{total} passed")

if __name__ == "__main__":
    test_reverse_string()