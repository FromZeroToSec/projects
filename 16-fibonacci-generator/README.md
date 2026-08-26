Fibonacci Generator

A Python script that calculates Fibonacci sequence numbers using two different approaches — iteration and recursion — and compares their execution time. Part of the FromZeroToSec Python training repo (Level 2 — Functions, strings, data manipulation).

What it does

The script calculates the nth Fibonacci number in two ways:

Iterative version (fibonacci_iterative): uses a loop to build up the sequence step by step.
Recursive version (fibonacci_recursive): calls itself with smaller values until it reaches a base case (n == 0 or n == 1).

Both versions are run on the same input and timed, showing how much slower plain recursion becomes compared to iteration as n grows.

Usage

Run the script:

bash
python3 main.py

Example output:

Iterative result: 832040
Iterative time: 1.5735626220703125e-05
Recursive result: 832040
Recursive time: 0.08486080169677734

Both functions return the same result, but the recursive version takes thousands of times longer — because it recalculates the same values over and over instead of reusing them.

What this demonstrates
Understanding the difference between iterative and recursive approaches to the same problem
Writing a recursive function with a proper base case to avoid infinite recursion
Measuring code performance in Python using the time module
Structuring reusable functions instead of writing logic directly in main()
Clean function documentation with docstrings and comments
Tech stack
Python 3
time — Python standard library
