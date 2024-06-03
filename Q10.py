Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bell_number(n):
...     bell = [[0 for i in range(n+1)] for j in range(n+1)]
...     bell[0][0] = 1
... 
...     for i in range(1, n+1):
...         # Explicitly put the last entry of the previous row to the first entry of this row
...         bell[i][0] = bell[i-1][i-1]
... 
...         # Fill the rest of the entries in the current row
...         for j in range(1, i+1):
...             bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
... 
...     return bell[n][0]
... 
... # Calculate the Bell number for 100
... result = bell_number(100)
... print(f"The number of ways to group sixty black objects and forty white objects is: {result}")
