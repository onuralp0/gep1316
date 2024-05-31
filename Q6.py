Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> def sieve_of_eratosthenes(limit):
... ...     is_prime = [True] * (limit + 1)
... ...     is_prime[0] = is_prime[1] = False
... ...     for p in range(2, int(limit**0.5) + 1):
... ...         if is_prime[p]:
... ...             for i in range(p * p, limit + 1, p):
... ...                 is_prime[i] = False
... ...     return [p for p, prime in enumerate(is_prime) if prime]
... ...
... >>> def find_first_value_with_over_k_ways(k):
... ...     limit = 1000  # Initial guess; we'll adjust if necessary
... ...     primes = sieve_of_eratosthenes(limit)
... ...
... ...     ways = [0] * (limit + 1)
... ...     ways[0] = 1  # There's one way to make 0: use no primes
... ...
... ...     for prime in primes:
... ...         for i in range(prime, limit + 1):
... ...             ways[i] += ways[i - prime]
... ...
... ...     # If the solution is not within the current limit, extend the search range
... ...     while max(ways) <= k:
... ...         limit *= 2
... ...         primes = sieve_of_eratosthenes(limit)
... ...
... ...         ways = [0] * (limit + 1)
... ...         ways[0] = 1
... ...
... ...         for prime in primes:
... ...             for i in range(prime, limit + 1):
... ...                 ways[i] += ways[i - prime]
... ...
... ...     for i in range(len(ways)):
... ...         if ways[i] > k:
... ...             return i
... ...
... >>> k = 5000
... >>> result = find_first_value_with_over_k_ways(k)
... >>> print(f"The first value which can be written as the sum of primes in over {k} different ways is: {result}")
