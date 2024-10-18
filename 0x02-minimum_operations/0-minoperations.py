#!/usr/bin/python3
'''

Module for the minimum operations problem

'''


def minOperations(n):
    '''
    returns sum of prime factors
    '''
    if n <= 1:
        return 0
    factors_sum = 0
    while n % 2 == 0:
        factors_sum += 2
        n //= 2
    for i in range(3, int(n ** 0.5) + 2, 2):
        while n % i == 0:
            factors_sum += i
            n //= i
    if n > 2:
        factors_sum += n
    return factors_sum
