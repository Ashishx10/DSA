# DSA

A structured collection of solved [LeetCode](https://leetcode.com) problems, organized by algorithmic pattern. Each problem folder contains the LeetCode prompt and a Python solution.

## Patterns

- [Sliding Window](#sliding-window) — 13 problems
- Two Pointers — coming soon
- Binary Search — coming soon
- Dynamic Programming — coming soon

## Sliding Window

| # | Problem | Difficulty | Sub-pattern | Time | Space |
|---|---------|:----------:|-------------|:----:|:-----:|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | Easy | Fixed window (min tracking) | O(n) | O(1) |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i) | Easy | Fixed window | O(n) | O(1) |
| 1046 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii) | Medium | Variable window (count constraint) | O(n) | O(1) |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum) | Medium | Variable window (sum constraint) | O(n) | O(1) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | Variable window + hash set | O(n) | O(min(n, alphabet)) |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) | Medium | Variable window + frequency count | O(n) | O(26) → O(1) |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string) | Medium | Fixed window + frequency match | O(n) | O(26) → O(1) |
| 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string) | Medium | Fixed window + frequency match | O(n) | O(26) → O(1) |
| 187 | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences) | Medium | Fixed window + hash set | O(n) | O(n) |
| 2017 | [Minimum Number of Flips to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating) | Medium | Fixed window + circular array | O(n) | O(1) |
| 1966 | [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element) | Medium | Variable window + sort | O(n log n) | O(1) |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) | Hard | Variable window + frequency match | O(m + n) | O(m + n) |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum) | Hard | Fixed window + monotonic deque | O(n) | O(k) |

## Structure

```
<Pattern>/<leetcode-number>-<problem-slug>/
├── README.md          # Problem statement (pulled from LeetCode)
└── <problem-slug>.py  # Solution
```

## Notes

- Space complexities marked `O(26) → O(1)` use a fixed-size array/hashmap bounded by the alphabet (26 lowercase letters), which is constant regardless of input size.
- "Fixed window" problems have a window size determined by the problem (`k`, or the length of a target string); "variable window" problems grow and shrink the window based on a constraint evaluated at each step.
