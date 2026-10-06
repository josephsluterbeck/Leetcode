# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

import random
import string
import time

# SOLUTION
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ''.join([char for char in s if char.isalnum()])

        l, r = 0, len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True

# TEST
def test_is_palindrome():
    sol = Solution()
    cases = [
        # (input, expected)
        ("A man, a plan, a canal: Panama", True),   # LeetCode example 1
        ("race a car", False),                      # LeetCode example 2
        (" ", True),                                # LeetCode example 3: empty after cleaning
        ("", True),                                 # empty string
        ("a", True),                                # single character
        ("aba", True),                              # odd length
        ("abba", True),                             # even length
        ("abca", False),                            # outer pair matches, inner doesn't
        ("Aa", True),                               # case-insensitive
        ("0P", False),                              # digit vs letter
        ("ab_a", True),                             # underscore is not alphanumeric
        (".,", True),                               # only punctuation
        ("No 'x' in Nixon", True),                  # quotes and spaces
        ("12321", True),                            # digits only
        ("123ab321", False),                        # mismatch in the middle
    ]
 
    passed = 0
    total = len(cases)
 
    for i, (s, expected) in enumerate(cases, 1):
        got = sol.isPalindrome(s)
        if got == expected:
            passed += 1
            print(f"PASS {i}: {s!r} -> {got}")
        else:
            print(f"FAIL {i}: {s!r} -> got {got}, expected {expected}")
 
    random.seed(125)
    chars = string.ascii_letters + string.digits
    half = ''.join(random.choice(chars) for _ in range(10**5))
    noisy_half = ''.join(c + random.choice(" ,.:!") for c in half[:50_000])
 
    big_cases = [
        ("2*10^5 palindrome", half + half[::-1], True),
        ("2*10^5 mismatch in middle", half + "X" + "Y" + half[::-1], False),
        ("2*10^5 mismatch at ends", "a" + half + half[::-1] + "b", False),
        ("2*10^5 all spaces/punctuation", " ,.:" * 50_000, True),
        ("2*10^5 noisy mixed-case palindrome", noisy_half + noisy_half[::-1].swapcase(), True),
    ]
 
    for name, s, expected in big_cases:
        total += 1
        start = time.perf_counter()
        got = sol.isPalindrome(s)
        elapsed = time.perf_counter() - start
        if got == expected:
            passed += 1
            print(f"PASS big: {name} in {elapsed:.3f}s")
        else:
            print(f"FAIL big: {name} -> got {got}, expected {expected} ({elapsed:.3f}s)")
 
    print(f"\n{passed}/{total} passed")
 
if __name__ == "__main__":
    test_is_palindrome()