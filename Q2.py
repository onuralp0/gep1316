Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... Type "help", "copyright", "credits" or "license" for more information.
... >>> def sum_of_even_fibonacci(limit):
... ...     a, b = 1, 2
... ...     total_sum = 0
... ...
... ...     while a <= limit:
... ...         if a % 2 == 0:
... ...             total_sum += a
... ...         a, b = b, a + b  # Generate the next term in the sequence
... ...
... ...     return total_sum
... ...
... >>> # Calculate the sum of even-valued terms in the Fibonacci sequence up to 4 million
... >>> result = sum_of_even_fibonacci(4000000)
... >>> print("The sum of even-valued terms in the Fibonacci sequence below 4 million is:", result)
... The sum of even-valued terms in the Fibonacci sequence below 4 million is: 4613732
