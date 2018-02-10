# @author = UT
# 9th Feb 2018
#nerd_heaven

# An exponential time implementation of calculating fibonnaci numbers
# It is very slow :(
def fib(n):
    return 1 if n <= 1 else fib(n-1)+fib(n-2)

# A linear time implementation of calculating fibonnaci numbers
# Good speed
def fib_linear(n):
    if n <= 1: return 1
    p = 0
    c = 1
    i = 2
    while i < n:
        fibi = c + p
        p = c
        c = fibi
        i += 1
    return c + p

# A constant time implementation of calculating fibonnaci numbers
# This shit is fast ;)
from math import sqrt
def fib_constant(n):
    phi = (1 + sqrt(5))/2
    phip = (1 - sqrt(5))/2
    return (phi**n - phip**n)/sqrt(5)
