Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import permutations, product
... from math import factorial
... 
... def count_valid_numbers():
...     digit_counts = range(4)  # each digit can appear 0, 1, 2, or 3 times
...     valid_combinations = []
... 
...     # Generate all valid combinations of digit counts that sum up to 18
...     for counts in product(digit_counts, repeat=10):
...         if sum(counts) == 18:
...             valid_combinations.append(counts)
... 
...     total_count = 0
...     
...     def num_permutations(counts):
...         n = sum(counts)
...         perm = factorial(n)
...         for count in counts:
...             if count > 1:
...                 perm //= factorial(count)
...         return perm
...     
...     # Calculate the total number of permutations for each valid combination
...     for counts in valid_combinations:
...         if counts[0] > 3:
...             continue
...         total_count += num_permutations(counts)
...         
...         # Adjust for leading zero
...         if counts[0] > 0:
...             counts_without_zero = list(counts)
...             counts_without_zero[0] -= 1
...             total_count -= num_permutations(counts_without_zero)
...     
...     return total_count
... 
... result = count_valid_numbers()
... print(f"The number of 18-digit numbers such that no digit occurs more than three times is: {result}")
