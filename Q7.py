Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... Type "help", "copyright", "credits" or "license" for more information.
... >>> def is_bouncy(number):
... ...     num_str = str(number)
... ...     increasing = decreasing = False
... ...
... ...     for i in range(len(num_str) - 1):
... ...         if num_str[i] < num_str[i + 1]:
... ...             increasing = True
... ...         elif num_str[i] > num_str[i + 1]:
... ...             decreasing = True
... ...
... ...         if increasing and decreasing:
... ...             return True
... ...     return False
... ...
... >>> def find_least_bouncy_proportion(target_proportion):
... ...     count_bouncy = 0
... ...     number = 100  # Starting from the first number that can be bouncy
... ...
... ...     while True:
... ...         if is_bouncy(number):
... ...             count_bouncy += 1
... ...
... ...         proportion = count_bouncy / number
... ...
... ...         if proportion == target_proportion:
... ...             return number
... ...
... ...         number += 1
... ...
... >>> # Find the least number for which the proportion of bouncy numbers is exactly 99%
... >>> target_proportion = 0.99
... >>> result = find_least_bouncy_proportion(target_proportion)
... >>> print(f"The least number for which the proportion of bouncy numbers is exactly 99% is: {result}")
... The least number for which the proportion of bouncy numbers is exactly 99% is: 1587000
