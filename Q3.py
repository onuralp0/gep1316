Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... Type "help", "copyright", "credits" or "license" for more information.
... >>> def largest_prime_factor(n):
... ...     # Start with the smallest prime factor
... ...     factor = 2
... ...     # Remove the factors of 2
... ...     while n % factor == 0:
... ...         n //= factor
... ...
... ...     # Check for odd factors from 3 onwards
... ...     factor = 3
... ...     while factor * factor <= n:
... ...         while n % factor == 0:
... ...             n //= factor
... ...         factor += 2
... ...
... ...     # If n becomes a prime number greater than 2
... ...     if n > 2:
... ...         return n
... ...     else:
... ...         return factor - 2
... ...
... >>> # The number to find the largest prime factor of
... >>> number = 600851475143
... >>> result = largest_prime_factor(number)
... >>> print("The largest prime factor of", number, "is:", result)
... The largest prime factor of 600851475143 is: 6857
