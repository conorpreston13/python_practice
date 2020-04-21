# Countdown Timer ==============================================================
print('Countdown Timer')

import time

def recur_countdown(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recur_countdown(n-1)

# ITERATIVE SOLUTION
# def iter_countdown(n):
#     while n >0:
#         print(n)
#         time.sleep(1)
#         n-= 1
#     print(n)

z = 5
print(f"Counting Down from {z}")
print(recur_countdown(z))
# print(iter_countdown(z)) ##Iterative solution call


# Factorial ====================================================================
print('Factorial') # n! = n * (n-1)!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = 0
print(f"The value of {f}! is {factorial(f)}")
f = 1
print(f"The value of {f}! is {factorial(f)}")
f = 5
print(f"The value of {f}! is {factorial(f)}")

# Fibonacci ====================================================================
print('Fibonacci')

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)


def fib_runner(fb):
    print(f"The {fb}th number in the fibonacci sequence is {fib_recur(fb)}")

fb = 0
fib_runner(fb)
fb = 4
fib_runner(fb)
fb = 10
fib_runner(fb)
