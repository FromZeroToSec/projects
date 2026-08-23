import time

def main():
    start = time.time()
    a = 0
    b = 1
    for i in range(10):
        print(a)
        old_a = a
        a = a + b
        b = old_a
        print(fibonacci_recursive(i))
    print(f"Iterative time: {time.time() - start}")
    start = time.time()
    print(fibonacci_recursive(10))
    print(f"Recursive time: {time.time() - start}")


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    main()