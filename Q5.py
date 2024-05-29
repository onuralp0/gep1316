Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... Type "help", "copyright", "credits" or "license" for more information.
... >>> def is_prime(n):
... ...     if n <= 1:
... ...         return False
... ...     if n == 2:
... ...         return True
... ...     if n % 2 == 0:
... ...         return False
... ...     for i in range(3, int(n ** 0.5) + 1, 2):
... ...         if n % i == 0:
... ...             return False
... ...     return True
... ...
... >>> def find_nth_prime(n):
... ...     count = 1  # Start from the first prime number, which is 2
... ...     candidate = 3  # Start checking odd numbers after 2
... ...     while True:
... ...         if is_prime(candidate):
... ...             count += 1
... ...         if count == n:
... ...             return candidate
... ...         candidate += 2  # Move to the next odd number
... ...
... >>> # Find the 10001st prime number
... >>> result = find_nth_prime(10001)
... >>> print("The 10001st prime number is:", result)
... The 10001st prime number is: 104743
