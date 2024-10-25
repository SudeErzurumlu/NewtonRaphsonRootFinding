# newton_raphson.py

def newton_raphson(f, f_prime, x0, tolerance=1e-7, max_iter=1000):
    """
    Finds the root of a function using the Newton-Raphson method.

    Args:
        f (callable): The function for which to find the root.
        f_prime (callable): The derivative of `f`.
        x0 (float): Initial guess.
        tolerance (float): Desired precision.
        max_iter (int): Maximum iterations allowed.

    Returns:
        float: Estimated root.

    Raises:
        ValueError: If the derivative is zero or max iterations reached.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)

        if abs(fpx) < 1e-12:
            raise ValueError("Derivative near zero; method may fail.")

        x_next = x - fx / fpx
        
        if abs(x_next - x) < tolerance:
            return x_next

        x = x_next

    raise ValueError("Maximum iterations reached without convergence.")
