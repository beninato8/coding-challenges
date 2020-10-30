#!/usr/bin/env python3

'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words
'''

def palindrome_permutation(string): # O(n)
    if len(string) < 2: # any single character or empty string
        return True
    counts = [string.count(c) for c in set(string) if c != ' '] # 'tacocat' -> [2,2,2,1]
    if all(n % 2 == 0 for n in counts): # all characters have an even count
        return True
    return [n % 2 == 1 for n in counts].count(True) == 1 # only 1 character can have odd count