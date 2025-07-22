# Data Structures and Algorithms Practice

This repository contains various DSA problems and their solutions implemented in Python.

## Arrays

1. **Two Sums (`01_Two_Sums.py`)**
   - Problem: Find two numbers that add up to a target
   - Solution: Uses hash map approach with O(n) time complexity
   - LeetCode problem

2. **Median of Sorted Arrays (`04_Median_Sorted_Array.py`)**
   - Problem: Find median of two sorted arrays
   - Implementation: Both brute force O((n+m)log(n+m)) and optimized binary search O(log(min(n,m)))

3. **Palindrome Number (`09_Palindrome.py`)**
   - Problem: Check if number is palindrome
   - Two implementations: String conversion and mathematical approach

4. **Longest Common Prefix (`14_Longest_Common_Prefix.py`)**
   - Problem: Find longest common prefix among array of strings
   - Implementation: Linear traversal with prefix reduction

5. **Three Sum (`15_Three_Sum.py`)**
   - Problem: Find triplets that sum to zero
   - Implementation: Sorting with two-pointer approach

6. **Four Sum (`18_Four_Sum.py`)**
   - Problem: Find quadruplets that sum to target
   - Implementation: Sorting with nested loops and two pointers

## Code Chef Problems

1. **Alternate Case Generator (`Alternate_Case_generator.py`)**
   - Converts string to alternate case format
   - Uses enumeration for character processing

2. **Divisible Number Finder (`Divisible_number_Finder.py`)**
   - Finds numbers divisible by given divisor in a range
   - Returns list of divisible numbers

3. **String Reversal (`String_reversal.py`)**
   - Reverses input strings using lambda functions
   - Implements string slicing technique

4. **Word Length Filter (`Word_length_filter.py`)**
   - Filters words based on minimum length
   - Uses generator expressions for memory efficiency

## Codeforces

1. **Mountain Problem (`mountain.py`)**
   - Division 3 contest problem (July 17, 2024)
   - Implements sliding window approach
   - Counts sequences of zeros with specific conditions

## Take You Forward

1. **Basic Problems**
   - **Reverse Number (`basics/reverse_number.py`)**
     - Reverses a given integer
     - Handles trailing zeros
     - Mathematical approach without string conversion

2. **Practice Problems (`practice.py`)**
   - Contains digit counting implementation
   - Uses iterative approach
   - Time Complexity: O(log n)

## How to Use

1. Each file contains detailed problem statement in comments
2. Solutions are implemented in Python 3
3. Most files include test cases and example outputs
4. Many solutions include both brute force and optimized approaches

## Testing

- Run individual files to test specific solutions
- Input format is specified in file comments
- Test cases are provided at the end of most files
