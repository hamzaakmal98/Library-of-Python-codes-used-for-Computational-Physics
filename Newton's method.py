def newton_method(f, f_prime, x0, tol, max_iter):
    """
    Finds the root of the function `f` using Newton's method.

    Parameters:
    f (function): The function for which we want to find the root.
    f_prime (function): The derivative of the function `f`.
    x0 (float): The initial guess for the root.
    tol (float): The tolerance (i.e. the desired accuracy).
    max_iter (int): The maximum number of iterations to perform.

    Returns:
    float: The approximate root of the function `f`.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fx_prime = f_prime(x)
        x -= fx / fx_prime
        if abs(fx) < tol:
            return x
    raise ValueError("Failed to converge after {} iterations".format(max_iter))


# Testing the newton_method function with some test cases
def test_newton_method():
    # Test case 1: Find the square root of 2
    f = lambda x: x**2 - 2
    f_prime = lambda x: 2*x
    x0 = 1.0
    tol = 1e-6
    max_iter = 100
    expected_root = 1.414213562373095
    computed_root = newton_method(f, f_prime, x0, tol, max_iter)
    print(f"Test case 1: Computed root = {computed_root}")
    assert abs(computed_root - expected_root) < tol

    # Test case 2: Find the root of x^3 - x - 1
    f = lambda x: x**3 - x - 1
    f_prime = lambda x: 3*x**2 - 1
    x0 = 1.5
    tol = 1e-8
    max_iter = 100
    expected_root = 1.324717957244746
    computed_root = newton_method(f, f_prime, x0, tol, max_iter)
    print(f"Test case 2: Computed root = {computed_root}")
    assert abs(computed_root - expected_root) < tol

    # Test case 3: Find the root of sin(x)
    from math import sin, cos
    f = sin
    f_prime = cos
    x0 = 1.0
    tol = 1e-6
    max_iter = 100
    expected_root = 0.0
    computed_root = newton_method(f, f_prime, x0, tol, max_iter)
    print(f"Test case 3: Computed root = {computed_root}")
    assert abs(computed_root - expected_root) < tol

    print("All tests passed!")


# Run the test function
test_newton_method()
