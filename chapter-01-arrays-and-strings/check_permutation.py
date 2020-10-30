#!/usr/bin/env python3

'''
Given two strings, write a method to decide if one is a permutation of the other
'''

def check_permutation(s1, s2): # O(nlogn)
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def check_permutation_1(s1, s2): # O(n)
    if len(s1) != len(s2):
        return False
    return {c:s1.count(c) for c in set(s1)} == {c:s2.count(c) for c in set(s2)}

def check_permutation_2(s1, s2): # O(n)
    if len(s1) != len(s2):
        return False
    counts = {c:s1.count(c) for c in set(s1)}
    for c in s2:
        if s2.count(c) != counts[c]:
            return False
    return True