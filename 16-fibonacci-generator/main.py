import time


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        old_a = a
        a = a + b
        b = old_a 
    return a



def main():
    start = time.time()
    print("Résultat itératif :", fibonacci_iterative(30))
    print("Temps itératif :", time.time() - start)
    start = time.time()
    print("Résultat récursif :", fibonacci_recursive(30))
    print("Temps récursif :", time.time() - start)


if __name__ == "__main__":
    main()