#!/usr/bin/python3
'''

The prime game module in Python

'''


def check_prime(value: int) -> bool:
    '''checks if a number is prime'''
    if value <= 1:
        return False
    for div in range(2, int(value**0.5) + 1):
        if value % div == 0:
            return False
    return True


def get_prime_numbers(ceil: int) -> list:
    '''gets prime numbers from 1 to n'''
    prime_numbers = []
    for i in range(1, ceil + 1):
        if check_prime(i):
            prime_numbers.append(i)
    return prime_numbers


def get_winner(num: int) -> int:
    '''gets the winner of a single game'''
    prime_values = get_prime_numbers(num)
    return 0 if len(prime_values) % 2 == 0 else 1


def isWinner(x, nums):
    '''determines the winner of the set of prime games'''
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    winners = ('Ben', 'Maria')
    win_count = {'Ben': 0, 'Maria': 0}
    for i in range(x):
        win_idx = get_winner(nums[i])
        win_count[winners[win_idx]] += 1
    if win_count['Maria'] == win_count['Ben']:
        return None
    return 'Maria' if win_count['Maria'] > win_count['Ben'] else 'Ben'
