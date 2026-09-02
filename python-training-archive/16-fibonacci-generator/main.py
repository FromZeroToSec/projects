import time


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    """
    # Base cases: the first two Fibonacci numbers
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Call the function for the two previous numbers
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    """
    a = 0
    b = 1

    # Repeat the calculation n times
    for i in range(n):
        # Save the old value of a before changing it
        old_a = a
        a = a + b
        b = old_a

    return a


def main():
    # Measure the execution time of the iterative version
    start = time.time()
    print("Iterative result:", fibonacci_iterative(30))
    print("Iterative time:", time.time() - start)

    # Measure the execution time of the recursive version
    start = time.time()
    print("Recursive result:", fibonacci_recursive(30))
    print("Recursive time:", time.time() - start)


if __name__ == "__main__":
    main()