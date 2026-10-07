# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.

import random
import time

# SOLUTION
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        built = list(s)

        l, r = 0, len(built) - 1
        while l < r:
            if built[l] not in vowels:
                l += 1
            elif built[r] not in vowels:
                r -= 1
            else:
                built[l], built[r] = built[r], built[l]
                l += 1
                r -= 1
        return ''.join(built)

# TEST
def reference(s):
    vowels = set("aeiouAEIOU")
    found = [c for c in s if c in vowels]
    return ''.join(found.pop() if c in vowels else c for c in s)
 
 
def test_reverse_vowels():
    sol = Solution()
    cases = [
        # (input, expected)
        ("IceCreAm", "AceCreIm"),        # LeetCode example 1
        ("leetcode", "leotcede"),        # LeetCode example 2
        ("hello", "holle"),
        ("a", "a"),                      # single vowel
        ("b", "b"),                      # single consonant
        ("bcd", "bcd"),                  # no vowels
        ("aeiou", "uoiea"),              # all vowels
        ("aA", "Aa"),                    # mixed case swaps
        ("ab", "ab"),                    # one vowel can't move
        ("race car", "race car"),        # palindrome vowels stay the same
        ("a.b,e!", "e.b,a!"),            # punctuation stays put
        ("Yo! Bye", "Ye! Byo"),          # "y" is NOT a vowel here
        ("12a34E", "12E34a"),            # digits stay put
        ("  ", "  "),                    # only spaces
    ]
 
    passed = 0
    total = len(cases)
 
    for i, (s, expected) in enumerate(cases, 1):
        got = sol.reverseVowels(s)
        if got == expected:
            passed += 1
            print(f"PASS {i}: {s!r} -> {got!r}")
        else:
            print(f"FAIL {i}: {s!r} -> got {got!r}, expected {expected!r}")

    random.seed(345)
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!?0123456789"
    big_cases = [
        ("3*10^5 random printable", ''.join(random.choice(letters) for _ in range(3 * 10**5))),
        ("3*10^5 all vowels", ''.join(random.choice("aeiouAEIOU") for _ in range(3 * 10**5))),
        ("3*10^5 no vowels", ''.join(random.choice("bcdfghjklmnpqrstvwxyz") for _ in range(3 * 10**5))),
        ("3*10^5 vowels only at the ends", "a" + "x" * (3 * 10**5 - 2) + "E"),
    ]
 
    for name, s in big_cases:
        total += 1
        expected = reference(s)
        start = time.perf_counter()
        got = sol.reverseVowels(s)
        elapsed = time.perf_counter() - start
        if got == expected:
            passed += 1
            print(f"PASS big: {name} in {elapsed:.3f}s")
        else:
            print(f"FAIL big: {name} ({elapsed:.3f}s)")
 
    print(f"\n{passed}/{total} passed")

if __name__ == "__main__":
    test_reverse_vowels()