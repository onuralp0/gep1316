Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> def sum_of_multiples(limit):
... ...     total_sum = 0
... ...     for number in range(1, limit):
... ...         if number % 3 == 0 or number % 5 == 0:
... ...             total_sum += number
... ...     return total_sum
... ...
... >>> # Calculate the sum of all multiples of 3 or 5 below 1000
... >>> result = sum_of_multiples(1000)
... >>> print("The sum of all multiples of 3 or 5 below 1000 is:", result)
... The sum of all multiples of 3 or 5 below 1000 is: 233168
... >>>Explanation of the code:
... 
... The function sum_of_multiples takes one argument limit, which defines the upper limit (1000 in this case).
... total_sum is initialized to 0 to store the cumulative sum of multiples.
... A for loop iterates over each number from 1 to limit - 1 (999).
... The condition if number % 3 == 0 or number % 5 == 0 checks if the number is a multiple of 3 or 5.
... If the condition is true, the number is added to total_sum.
... After the loop finishes, the function returns the total sum.
... The result is printed to the console.
