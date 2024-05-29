Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... Type "help", "copyright", "credits" or "license" for more information.
... >>> def is_palindrome(number):
... ...     return str(number) == str(number)[::-1]
... ...
... >>> def largest_palindrome_product():
... ...     max_palindrome = 0
... ...
... ...     # Iterate over all products of two 3-digit numbers
... ...     for i in range(100, 1000):
... ...         for j in range(i, 1000):  # Start j from i to avoid duplicate pairs
... ...             product = i * j
... ...             if is_palindrome(product) and product > max_palindrome:
... ...                 max_palindrome = product
... ...
... ...     return max_palindrome
... ...
... >>> result = largest_palindrome_product()
... >>> print("The largest palindrome made from the product of two 3-digit numbers is:", result)
... The largest palindrome made from the product of two 3-digit numbers is: 906609
