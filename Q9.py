s = 0
k = 1
delta = 1

while delta > 1e-10:
    term = 1 / (k ** 2)
    s_new = s + term

    delta = abs(s_new - s)

    s = s_new
    k += 1

print(s)
nmaxd = k
print(f"The integer where it terminates is {k}")

# Part b

# The maximum integer `k` used in the summation is related to the number of terms that need to be added in order to
# obtain a good approximation of the sum. In general, the more terms we add, the closer our approximation will be to
# the true value of the sum. However, because the sum converges very slowly, we need to add a very large number of
# terms to obtain a good approximation.
#
# In practice, we can often stop adding terms once the contribution of each additional term becomes very small. The
# threshold for stopping depends on the desired accuracy of the approximation (1e-10 in this case).
#
# Therefore, the value of k will be egregiously close to the 1/square root of closeness threshold



nUpperLimit = 40000000
# Change this nmaxd to 4, 8, 16, 32 and perform calculations.
nmaxd = 4

sum_old = 0
nmax = nUpperLimit // nmaxd
for k in range(1, nmax + 1):
    sum_old += 1 / k ** 2
sum_new = sum_old
n = nmax
while abs(sum_new - sum_old) > 1e-10:
    sum_old = sum_new
    for k in range(n + 1, n + 1 + nmaxd):
        sum_new += 1 / k ** 2
    n += nmaxd

print("The sum is:", sum_new)


def kahan_sum_basel(nmax):
    sum_ = 0.0
    c = 0.0
    for k in range(1, nmax + 1):
        y = 1.0 / (k * k) - c
        t = sum_ + y
        c = (t - sum_) - y
        sum_ = t
    return sum_

# Increasing nmax will increase the accuracy of the sum. For n -> we get the accurate result of pi^2/6
nmax = 10000000
kahan_sum = kahan_sum_basel(nmax)
print(kahan_sum)
