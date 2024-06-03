Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... def is_square(n):
...     return int(math.sqrt(n)) ** 2 == n
... 
... def find_smallest_sum():
...     min_sum = float('inf')
...     limit = 100  # Arbitrary limit, can be increased for a more exhaustive search
... 
...     for a in range(1, limit):
...         for b in range(a-1, 0, -1):
...             if not is_square(a*a - b*b):
...                 continue
...             for c in range(a, limit):
...                 for d in range(c-1, 0, -1):
...                     if not is_square(c*c - d*d):
...                         continue
...                     for e in range(1, limit):
...                         for f in range(e-1, 0, -1):
...                             if not (is_square(e*e + f*f) and is_square(e*e - f*f)):
...                                 continue
... 
...                             x1 = (a*a + b*b) // 2
...                             y1 = (a*a - b*b) // 2
...                             x2 = (c*c + d*d) // 2
...                             z1 = (c*c - d*d) // 2
...                             y2 = (e*e + f*f) // 2
...                             z2 = (e*e - f*f) // 2
... 
...                             if x1 == x2 and y1 == y2 and z1 == z2:
...                                 x, y, z = x1, y1, z1
...                                 if x > y > z > 0:
...                                     min_sum = min(min_sum, x + y + z)
...     return min_sum
... 
... result = find_smallest_sum()
... print(f"The smallest x+y+z is: {result}")
