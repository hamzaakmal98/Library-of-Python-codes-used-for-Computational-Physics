# # # Initialize variables
# # s = 0
# # k = 1
# # delta = 1
# #
# # # Loop until the sum stops changing
# # while delta > 1e-10:
# #     # Add the next term to the sum
# #     term = 1 / (k ** 2)
# #     s_new = s + term
# #
# #     # Compute the difference between the new and old sums
# #     delta = abs(s_new - s)
# #
# #     # Update the sum and the counter
# #     s = s_new
# #     k += 1
# #
# # # Print the final sum
# # print(s)
# #
# # nmaxd = s
# #
# # # #There is an interesting relationship between the value of the maximum integer `k` used in the summation and the value of the sum of the reciprocals of the squares of the positive integers.
# # #
# # # In fact, the value of the sum is equal to pi^2 / 6, where pi is the mathematical constant approximately equal to 3.14159... This relationship was discovered by the Swiss mathematician Leonhard Euler in the 18th century, and is known as the Basel problem.
# # #
# # # The maximum integer `k` used in the summation is related to the number of terms that need to be added in order to obtain a good approximation of the sum. In general, the more terms we add, the closer our approximation will be to the true value of the sum. However, because the sum converges very slowly, we need to add a very large number of terms to obtain a good approximation.
# # #
# # # In practice, we can often stop adding terms once the contribution of each additional term becomes very small. The threshold for stopping depends on the desired accuracy of the approximation. In the code I provided earlier, I used a threshold of `1e-10`, which is a reasonable choice for many applications.
#
# import time
#
# # Set the maximum integer to use in the summation
# nmaxr = 40000000
#
# # Set the factor by which nmaxr is divided to get the initial value of nmax for the loop
# nmaxd = 4
#
# # Calculate the sum of the reciprocals of the squares of the positive integers
# sum_old = 0
# nmax = nmaxr // nmaxd
# start_time = time.time()
# for k in range(1, nmax+1):
#     sum_old += 1/k**2
# sum_new = sum_old
# n = nmax
# while abs(sum_new - sum_old) > 1e-10:
#     sum_old = sum_new
#     for k in range(n+1, n+1+nmaxd):
#         sum_new += 1/k**2
#     n += nmaxd
# end_time = time.time()
#
# # Print the result and the time taken
# print("The sum is:", sum_new)
# print("Time taken:", end_time - start_time, "seconds")

def kahan_sum_basel(nmax):
    sum_ = 0.0
    c = 0.0
    for k in range(1, nmax + 1):
        y = 1.0 / (k*k) - c
        t = sum_ + y
        c = (t - sum_) - y
        sum_ = t
    return sum_

nmax = 1000000
kahan_sum = kahan_sum_basel(nmax)
print(kahan_sum)
