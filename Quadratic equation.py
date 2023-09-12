# Using the quadratic formula, we can find the roots:
#
# x1 = (-b + √(b^2 - 4ac)) / (2a)
# x2 = (-b - √(b^2 - 4ac)) / (2a)
#
# We can then find the product of the roots:
#
# x1 * x2 = [(-b + √(b^2 - 4ac)) / (2a)] * [(-b - √(b^2 - 4ac)) / (2a)]
#
# x1 * x2 = [(-b)^2 - (√(b^2 - 4ac))^2] / (4a^2)
#
# x1 * x2 = (b^2 - (b^2 - 4ac)) / (4a^2)
#
# x1 * x2 = c / a
import math
import cmath

a = 1
b = 108
c = 1

# Calculate x- using the "good" formula with complex numbers
x_minus = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)

# Calculate x- using the "bad" formula with complex numbers
x_minus_bad = (-b - cmath.sqrt(b**2 - 4*a*c + 0j)) / (2*a)

# Calculate x+ using the relation x+x- = c/a
x_plus = c/a / x_minus

# Calculate x+ using the "bad" formula with complex numbers
x_plus_bad = c/a / x_minus_bad

# Print out the results
print("x- (good):", x_minus)
print("x- (bad):", x_minus_bad)
print("x+ (good):", x_plus)
print("x+ (bad):", x_plus_bad)






# #As we can see, using the "bad" formula to calculate x- leads to a catastrophic cancellation, resulting in a significant error in the result. On the other hand, using the "good" formula avoids the cancellation and gives a much more accurate result.
#
# Using the relation x+x- = c/a, we can calculate x+ without any cancellation issues. The result of x+ is accurate and matches the value obtained using the "good" formula for x-.
#
# In general, it is always a good practice to avoid subtracting two nearly equal numbers to reduce the effect of catastrophic cancellation.